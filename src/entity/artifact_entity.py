from dataclasses import dataclass


# Data Ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    dataset_path: str

    def to_dict(self):
        return self.__dict__
