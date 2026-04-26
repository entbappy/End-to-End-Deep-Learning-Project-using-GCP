import os
import sys
from zipfile import ZipFile
from src.logger import logging
from src.exception import CustomException
from src.configurations.gcloud_syncer import GCloudSync
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        """
        :param data_ingestion_config: Configuration for data ingestion
        """
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync()

    def get_data_from_gcloud(self) -> None:

        """
        Method Name :   get_data_from_gcloud
        Description :   This function fetch data from gcloud

        Output      :   Returns data into DataIngestionArtifacts
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            logging.info("Entered the get_data_from_gcloud method of Data ingestion class")

            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)

            self.gcloud.sync_file_from_gcloud(self.data_ingestion_config.BUCKET_NAME,
                                              self.data_ingestion_config.ZIP_FILE_NAME,
                                              self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,)

            logging.info("Exited the get_data_from_gcloud method of Data ingestion class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def unzip_and_clean(self) -> None:
        """
        Method Name :   unzip_and_clean
        Description :   This function unzip the dataset

        Output      :   Returns Unzipped Data
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered the unzip_and_clean method of Data ingestion class")
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
            logging.info("Exited the unzip_and_clean method of Data ingestion class")
        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        """
        Method Name :   initiate_data_ingestion
        Description :   This function initiates a data ingestion steps

        Output      :   Returns data ingestion artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered the initiate_data_ingestion method of Data ingestion class")
        try:
            self.get_data_from_gcloud()
            logging.info("Fetched the zipped dataset from Gcloud Storage bucket")

            self.unzip_and_clean()
            logging.info("Unzipped the file fetched from Gcloud Storage bucket")

            logging.info("Deleting dataset.zip file")
            os.remove(os.path.join(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,
                                   self.data_ingestion_config.ZIP_FILE_NAME))

            data_ingestion_artifacts = DataIngestionArtifacts(
                dataset_path=self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            logging.info("Exited the initiate_data_ingestion method of Data ingestion class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
