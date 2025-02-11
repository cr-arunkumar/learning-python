import json
import psutil
import time
import threading
import logging
import requests
import argparse
from datetime import datetime
from typing import Dict, Any
import os

'''

pyinstaller- help us to create a single executable file that includes all the dependencies that can 
on any machine without installing python or any packages 

pyinstaller --onefile metrices_collector.py

---
tmux - can be used to run the script in a background process.
# installtion on MAC/Linux: 
# Mac OS : brew install tmux , for lunux system: apt-get install tmux
then-
cmd: tmux new-session -d -s server-monitor "python3 metrices_collector.py"
then ctrl+b : switch to new session
ctrl+d - detach the current session (exit from session and script will continue running in background)
'''

class MetricsCollector:
    def __init__(self, api_endpoint: str, interval: int = 1):
        self.api_endpoint = api_endpoint
        self.interval = interval
        self.setup_logging()

    
    def collect_top_processes_metrics(self, count: int = 10):
        try:
            processes = []
            for proc in psutil.process_iter():
                proc_info = {}
                try:
                    with proc.oneshot():
                        proc_info["pid"] = proc.pid
                        proc_info["ppid"] = proc.ppid()
                        proc_info["name"] = proc.name()
                        proc_info["exe"] = proc.exe()  
                        proc_info["cpu_percent"] = proc.cpu_percent()
                        mem_info = proc.memory_info()
                        proc_info["mem_rss"] = mem_info.rss
                        proc_info["mem_vms"] = mem_info.vms
                        proc_info["num_threads"] = proc.num_threads()
                        proc_info["nice_priority"] = proc.nice()
                    processes.append(proc_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            processes.sort(key=lambda p: p['mem_rss'], reverse=True)
            return processes[:count]
        except Exception as e:
            self.logger.error(f"Error collecting top processes metrics: {e}")
            return {'top_processes': []}
         
    
    def collect_top_folders_metrics(self, count: int = 10):
      try:
        root_directory = '/'
        folder_sizes = []

        for entry in os.scandir(root_directory):
            if entry.is_dir(follow_symlinks=False):
                try:
                    size = os.path.getsize(entry.path)
                    folder_sizes.append({'directory': entry.path, 'size': size})
                except Exception as e:
                    self.logger.warning(f"Error accessing directory {entry.path}: {e}")

        # Calculate total size and percentages
        total_size = sum(folder['size'] for folder in folder_sizes)

        for folder in folder_sizes:
            folder['percent_usage'] = (folder['size'] / total_size) * 100 if total_size > 0 else 0

        # Sort by size and return top N
        folder_sizes.sort(key=lambda x: x['size'], reverse=True)
        return folder_sizes[:count]

      except Exception as e:
        self.logger.error(f"Error collecting top folders metrics: {e}")
        return []





    def collect_active_connections_metrics(self, count: int = 10):
        try:
            connections = psutil.net_connections(kind='inet')
            active_connections = []
            try:
             for conn in connections:
                if conn.pid is None:
                        continue
                conn_info = {
                    'fd': conn.fd,
                    'family': conn.family.name,
                    'type': conn.type.name,
                    'laddr': f"{conn.laddr.ip}:{conn.laddr.port}", # type: ignore
                    'raddr': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
                    'status': conn.status
                }
                active_connections.append(conn_info)
            except psutil.AccessDenied:
                self.logger.warning("Permission denied while accessing network connections")
            # Return the top 'count' active connections
            return active_connections[:count]
        except psutil.AccessDenied:
                self.logger.warning("Permission denied while accessing network connections")
        except Exception as e:
            self.logger.error(f"Error collecting active connections metrics: {e}")
            return []

    def collect_network_traffic_metrics(self) -> Dict[str, Any]:
        try:
            net_io = psutil.net_io_counters()
            return {
                'bytes_sent': net_io.bytes_sent,
                'bytes_recv': net_io.bytes_recv,
                'packets_sent': net_io.packets_sent,
                'packets_recv': net_io.packets_recv,
                'errin': net_io.errin,
                'errout': net_io.errout,
                'dropin': net_io.dropin,
                'dropout': net_io.dropout
            }
        except psutil.AccessDenied:
            self.logger.warning("Permission denied while accessing network traffic metrics")
            return {}
        except Exception as e:
            self.logger.error(f"Error collecting network traffic metrics: {e}")
            return {}
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def collect_cpu_metrics(self) -> Dict[str, Any]:
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'cpu_count': psutil.cpu_count(),
            'cpu_freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else {},
            'cpu_stats': psutil.cpu_stats()._asdict(),
        }

    def collect_memory_metrics(self) -> Dict[str, Any]:
        memory = psutil.virtual_memory()
        return {
            'total': memory.total,
            'available': memory.available,
            'percent': memory.percent,
            'used': memory.used,
            'free': memory.free,
            'available': memory.available,
        }

    def collect_disk_metrics(self) -> Dict[str, Any]:
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        }

    def collect_network_metrics(self) -> Dict[str, Any]:
        return dict(psutil.net_io_counters()._asdict())

    def collect_load_average(self) -> Dict[str, Any]:
        load_avg = psutil.getloadavg()
        return {
            '1min': load_avg[0],
            '5min': load_avg[1],
            '15min': load_avg[2]
        }

    def collect_disk_io_metrics(self) -> Dict[str, Any]:
        return dict(psutil.disk_io_counters()._asdict()) # type: ignore

    def send_metrics(self, metrics: Dict[str, Any]):
        try:
            response = requests.post(self.api_endpoint, json=metrics)
            response.raise_for_status()
            self.logger.info("Metrics sent successfully")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending metrics: {e}")

    def collect_and_send_all_metrics(self):
        try:
            metrics = {
                'top_processes': self.collect_top_processes_metrics(),
                'top_folders': self.collect_top_folders_metrics(),
                'active_connections': self.collect_active_connections_metrics(),
                'network_traffic': self.collect_network_traffic_metrics(),
                'timestamp': datetime.now().isoformat(),
                'cpu': self.collect_cpu_metrics(),
                'memory': self.collect_memory_metrics(),
                'disk': self.collect_disk_metrics(),
                'network': self.collect_network_metrics(),
                'load_average': self.collect_load_average(),
                'disk_io': self.collect_disk_io_metrics()
            }
            print(f"Sending metrics to {json.dumps(metrics, indent=4)}\n")
            # self.send_metrics(metrics)
        except Exception as e:
            self.logger.error(f"Error in metrics collection: {e}")

    def start_collection(self):
        def collection_loop():
            while True:
                self.collect_and_send_all_metrics()
                time.sleep(self.interval)

        collection_thread = threading.Thread(target=collection_loop, daemon=True)
        collection_thread.start()
        self.logger.info(f"Started metrics collection with {self.interval} second interval")
        return collection_thread

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Metrics Collector')
    parser.add_argument('--api-endpoint', type=str, required=True, help='API endpoint to send metrics')
    parser.add_argument('--interval', type=int, default=1, help='Interval in seconds for metrics collection')
    args = parser.parse_args()

    collector = MetricsCollector(api_endpoint=args.api_endpoint, interval=args.interval)
    collector.start_collection()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping metrics collection...")
