import os, sys
from src.exception import CustomException


class GCloudSync:

    def sync_file_from_gcloud(self, gcp_bucket_url, filename, destination):
        """
        param gcp_bucket_url : GCP bucket url
        param filepath: filepath
        param destination: where to store
        """
        try:
            command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/"
            # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
            os.system(command)
        except Exception as e:
            raise CustomException(e, sys) from e

    def sync_file_to_gcloud(self, gcp_bucket_url, filepath):
        """
        param gcp_bucket_url : GCP bucket url
        param filepath: filepath
        """
        try:
            command = f"gsutil cp {filepath} gs://{gcp_bucket_url}/"
            # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
            os.system(command)
        except Exception as e:
            raise CustomException(e, sys) from e
