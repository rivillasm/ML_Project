from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os, sys


class DataValidation:

    def __init__(self, data_validation_config : DataValidationConfig,
                       data_ingestion_artifact : DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e, sys) from e

    # check if the training/test files are available
    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if train/test file exists")
            is_train_file_exist = False
            is_test_file_exist = False
            train_file_path = self.data_ingestion_artifact.train_file_path      # gets the paths
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist           # returns true or false
            logging.info(f"Is train and test file exists?-> {is_available}")

            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_validation(self):
        try:
            is_available = self.is_train_test_file_exists()
            if not is_available:
                training_file =
                testing_file =
                message = f""
                raise Exception("Trainig or Testing file is not available")
        except Exception as e:
            raise HousingException(e, sys) from e