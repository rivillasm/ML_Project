from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, \
    modelTrainerConfig, modelEvaluationConfig, modelPusherConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import *                 # import all declared functions within this file/library
from housing.exception import HousingException
import sys, os
from housing.logger import logging

class Configuration:

    def __init__(self, config_file_path:str =CONFIG_FILE_PATH,
                       current_time_stamp:str =CURRENT_TIME_STAMP) -> None:
        try:
            self.config_info = read_yaml_file(config_file_path)
            self.get_training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e,sys) from e


    def get_data_ingestion_config(self) -> DataIngestionConfig:   # calling the function you get the entity
        try:
            artifact_dir=self.get_training_pipeline_config.artifact_dir         # extracting the artifact directory name
            data_ingestion_artifact_dir = os.path.join(
                        artifact_dir,
                        DATA_INGESTION_ARTIFACT_DIR,
                        self.time_stamp)                                        # creates the entire directory path

            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]   # all info related to data ingestion

            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]   # extracts the url
            tgz_download_dir = os.path.join(
                        data_ingestion_artifact_dir,
                        data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])  # creates path for the data download

            raw_data_dir = os.path.join(
                        data_ingestion_artifact_dir,
                        data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])      # creates path for raw data

            ingested_data_dir = os.path.join(
                        data_ingestion_artifact_dir,
                        data_ingestion_info[DATA_INGESTION_DIR_NAME_KEY])           # creates path for data ingested


            self.config_info
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=,
                tgz_download_dir=,
                raw_data_dir=,
                ingested_train_dir=,
                ingested_test_dir=)
            logging.info(f"Data Ingestion config: {data_ingestion_config}")

        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> modelTrainerConfig:
        pass

    def get_model_evaluation_config(self) -> modelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> modelPusherConfig:
        pass

    def get_training_pipeline_config(self)-> TrainingPipelineConfig :
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                        training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info("Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise HousingException(e,sys) from e

