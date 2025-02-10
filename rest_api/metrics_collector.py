import psutil
import time
import sqlite3
from datetime import datetime
import json
import threading
import logging
from typing import Dict, Any

class MetricsCollector:
    def __init__(self, db_path: str = "metrics.db"):
        self.db_path = db_path
        self.setup_logging()
        self.setup_database()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def setup_database(self):
        """Initialize SQLite database and create necessary tables"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS system_metrics (
                        timestamp TEXT,
                        metric_type TEXT,
                        metric_value REAL,
                        additional_info TEXT
                    )
                ''')
                conn.commit()
                self.logger.info("Database initialized successfully")
        except sqlite3.Error as e:
            self.logger.error(f"Database initialization error: {e}")

    def collect_cpu_metrics(self) -> Dict[str, Any]:
        """Collect CPU-related metrics"""
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
            'free': memory.free
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

    def store_metrics(self, metric_type: str, metric_value: float, additional_info: Dict = None):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO system_metrics (timestamp, metric_type, metric_value, additional_info) VALUES (?, ?, ?, ?)',
                    (
                        datetime.now().isoformat(),
                        metric_type,
                        metric_value,
                        json.dumps(additional_info) if additional_info else None
                    )
                )
                conn.commit()
        except sqlite3.Error as e:
            self.logger.error(f"Error storing metrics: {e}")

    def collect_and_store_all_metrics(self):
        try:
            cpu_metrics = self.collect_cpu_metrics()
            memory_metrics = self.collect_memory_metrics()
            disk_metrics = self.collect_disk_metrics()
            network_metrics = self.collect_network_metrics()

            self.store_metrics('cpu_usage', cpu_metrics['cpu_percent'], 
                             {'cpu_count': cpu_metrics['cpu_count'], 'cpu_freq': cpu_metrics['cpu_freq']})

            self.store_metrics('memory_usage', memory_metrics['percent'], 
                             {'total': memory_metrics['total'], 'available': memory_metrics['available']})

            self.store_metrics('disk_usage', disk_metrics['percent'], 
                             {'total': disk_metrics['total'], 'free': disk_metrics['free']})

            self.store_metrics('network_io', network_metrics['bytes_sent'] + network_metrics['bytes_recv'], 
                             network_metrics)
            self.logger.info("Metrics collected and stored successfully")
        except Exception as e:
            self.logger.error(f"Error in metrics collection: {e}")

    def start_collection(self, interval: int = 1):
        """Start collecting metrics at specified interval"""
        def collection_loop():
            while True:
                self.collect_and_store_all_metrics()
                time.sleep(interval)

        collection_thread = threading.Thread(target=collection_loop, daemon=True)
        collection_thread.start()
        self.logger.info(f"Started metrics collection with {interval} second interval")
        return collection_thread

class MetricsRetriever:
    def __init__(self, db_path: str = "metrics.db"):
        self.db_path = db_path

    def get_metrics(self, metric_type: str = None, start_time: str = None, end_time: str = None) -> list:
        """Retrieve metrics from the database with optional filtering"""
        query = 'SELECT * FROM system_metrics WHERE 1=1'
        params = []

        if metric_type:
            query += ' AND metric_type = ?'
            params.append(metric_type)

        if start_time:
            query += ' AND timestamp >= ?'
            params.append(start_time)

        if end_time:
            query += ' AND timestamp <= ?'
            params.append(end_time)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def get_latest_metrics(self, metric_type: str = None) -> dict:
        query = '''
            SELECT m1.*
            FROM system_metrics m1
            LEFT JOIN system_metrics m2
            ON m1.metric_type = m2.metric_type
            AND m1.timestamp < m2.timestamp
            WHERE m2.timestamp IS NULL
        '''
        
        if metric_type:
            query += ' AND m1.metric_type = ?'
            params = (metric_type,)
        else:
            params = ()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            
            return {
                row[1]: {
                    'timestamp': row[0],
                    'value': row[2],
                    'additional_info': json.loads(row[3]) if row[3] else None
                }
                for row in results
            }

if __name__ == "__main__":
    # Initialize collector
    collector = MetricsCollector()
    
    collection_thread = collector.start_collection(interval=2)
    
    # Initialize retriever
    retriever = MetricsRetriever()
    
    try:
        while True:
            latest_metrics = retriever.get_latest_metrics()
            print("\nLatest Metrics:")
            print("==",json.dumps(latest_metrics, indent=2))
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopping metrics collection...")