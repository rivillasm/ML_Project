from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import sys, os
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator , TransformerMixin   # base class for all estimators in scikit-learn
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from housing.util.util import read_yaml_file
from housing.constant import *


# longitude: float
# latitude: float
# housing_median_age: float
# total_rooms: float
# total_bedrooms: float
# population: float
# households: float
# median_income: float
# median_house_value: float
# ocean_proximity : category
# income_cat: float

class FeatureGenerator(BaseEstimator, TransformerMixin):   # custom generator
    def __init__(self, add_bedrooms_per_room=True,
                 total_rooms_ix=3,
                 population_ix=5,
                 households_ix=6,
                 total_bedrooms_ix=4, columns=None):
        """
        FeatureGenerator Initialization
        add_bedrooms_per_room: bool
        total_rooms_ix: int index number of total rooms columns
        population_ix: int index number of total population columns
        households_ix: int index number of households columns
        total_bedrooms_ix: int index number of bedrooms columns
        """
        try:
            self.columns = columns
            if self.columns is not None:
                total_rooms_ix= self.columns.index(COLUMN_TOTAL_ROOMS)
                population_ix=self.columns.index(COLUMN_POPULATION)
                households_ix=self.columns.index(COLUMN_HOUSEHOLDS)
                total_bedrooms_ix=self.columns.index(COLUMN_TOTAL_BEDROOM)

            self.add_bedrooms_per_room= add_bedrooms_per_room
            self.total_rooms_ix= total_rooms_ix
            self.population_ix= population_ix
            self.households_ix= households_ix
            self.total_bedrooms_ix= total_bedrooms_ix

        except Exception as e:
            raise HousingException(e,sys) from e


    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        try:
            room_per_household = X[:,self.total_rooms_ix] / X[:,self.households_ix]
            population_per_household = X[:,self.population_ix] / X[:,self.households_ix]
            bedrooms_per_room = X[:,self.total_bedrooms_ix] / X[:,self.total_rooms_ix]
            if self.add_bedrooms_per_room:
                # concatenates the different variables
                generated_feature = np.c[X, room_per_household, population_per_household,bedrooms_per_room]
            else:
                generated_feature = np.c[X, room_per_household, population_per_household]
            return generated_feature

        except Exception as e:
            raise HousingException(e,sys) from e



class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact : DataValidationArtifact):

        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact

        except Exception as e:
            raise HousingException(e,sys) from e

    # static method - it means the function is put inside the class but it cannot access the instance of that class
    # we don't even call the self part
    # no info from the class is used in the function under staticmethod
    @staticmethod
    def load_data(file_path: str, schema_file_path: str)->pd.DataFrame:
        try:
            dataset_schema = read_yaml_file(schema_file_path)   # reads the schema file
            schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]  # extract  the columns name and type key/values
            dataframe = pd.read_csv(file_path)
            error_message = ""

            for column in dataframe.column:
                if column in list(schema.keys()):
                    dataframe[column].astype(schema[column])   # assigns the datatype to the corresponding column
                else:
                    error_message=f"{error_message} \n Column: [{column}] is not in the schema."
            if len(error_message) > 0:
                raise Exception(error_message)
            return dataframe

        except Exception as e:
            raise HousingException(e,sys) from e