from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os, sys
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
import pandas as pd
import json



class DataValidation:

    def __init__(self, data_validation_config : DataValidationConfig,
                       data_ingestion_artifact : DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e, sys) from e


    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df, test_df

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

            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file {training_file} or Testing file {testing_file} is not present"
                raise Exception(message)

            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e


    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False
            validation_status = True

            # ***** PUT ASSIGNMENT HERE


            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e


    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection])  # creates an object from the Profile library

            train_df, test_df = self.get_train_and_test_df()  # gets the datasets

            profile.calculate(train_df,test_df)  # calculates profile

            report = json.loads(profile.json())  # used to parse a JSON string and convert it into a dictionary

            with open(self.data_validation_config.report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)   # saves the report

            return report

        except Exception as e:
            raise HousingException(e, sys) from e

    def save_data_drift_report_page(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_data_drift_found(self)->bool:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e




    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()
        except Exception as e:
            raise HousingException(e, sys) from e