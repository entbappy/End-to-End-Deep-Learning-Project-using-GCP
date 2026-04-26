from src.constants import *
from dataclasses import dataclass
from src.utils.main_utils import read_yaml_file


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.config = read_yaml_file(CONFIG_PATH)
        self.BUCKET_NAME: str = self.config['data_ingestion_config']["bucket_name"]
        self.ZIP_FILE_NAME: str = self.config['data_ingestion_config']["zip_file_name"]
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)

