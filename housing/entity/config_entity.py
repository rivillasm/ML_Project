from collections import namedtuple

# info necessary to collect the data
# here we define the structure for our configuration for every component in the pipeline

DataIngestionConfig = namedtuple("DataIngestionConfig",
        ["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",
        ["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_files_path"])
# preprocessed_object_files_path - where the pickled file for the preprocessed data gets saved.
# add_bedroom_per_room - a column to be added to the dataset

modelTrainerConfig = namedtuple("modelTrainerConfig",
        ["trained_model_file_path","base_accuracy"])
# trained_model_file_path - trained model pickle file location

modelEvaluationConfig = namedtuple("modelEvaluationConfig",
        ["model_evaluation_file_path","time_stamp"])

modelPusherConfig = namedtuple("modelPusherConfig", ["expert_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])