import os
import logging
from datetime import datetime

Log_dir = 'logs'
os.makedirs(Log_dir, exist_ok=True)

Log_file = os.path.join(Log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=Log_file,
    level=logging.INFO,   
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)   
    return logger