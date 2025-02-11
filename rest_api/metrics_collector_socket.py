import json
import psutil
import time
import threading
import logging
import requests
import argparse
from datetime import datetime
from typing import Dict, Any
from websocket import create_connection, WebSocketException

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
    def __init__(self, websocket_url: str, interval: int = 1):
        self.websocket_url = websocket_url
        self.interval = interval
        self.setup_logging()

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
            ws = create_connection(self.websocket_url, sslopt={"cert_reqs": 0})
            ws.send(json.dumps(metrics))
            ws.close()
            self.logger.info("Metrics sent successfully via WebSocket")
        except WebSocketException as e:
            self.logger.error(f"Error sending metrics via WebSocket: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")


    def collect_and_send_all_metrics(self):
        try:
            metrics = {
                'timestamp': datetime.now().isoformat(),
                'cpu': self.collect_cpu_metrics(),
                'memory': self.collect_memory_metrics(),
                'disk': self.collect_disk_metrics(),
                'network': self.collect_network_metrics(),
                'load_average': self.collect_load_average(),
                'disk_io': self.collect_disk_io_metrics()
            }
            self.send_metrics(metrics)
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
    parser.add_argument('--websocket-url', type=str, required=True, help='WebSocket URL to send metrics')
    parser.add_argument('--interval', type=int, default=1, help='Interval in seconds for metrics collection')
    args = parser.parse_args()

    collector = MetricsCollector(websocket_url=args.websocket_url, interval=args.interval)
    collector.start_collection()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping metrics collection...")
