import logging
import os

from datetime import datetime

LOF_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

os.makedirs(os.path.join(os.getcwd(), "logs"), exist_ok=True)

logs_dir_path = os.path.join(os.getcwd(), "logs")

LOG_FILE_PATH = os.path.join(logs_dir_path, LOF_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
