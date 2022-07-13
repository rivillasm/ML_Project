import yaml
from housing.exception import HousingException
import os, sys
import numpy as np
import dill
import pandas as pd
from housing.constant import *


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns the contents as a dictionary
    file_path:str
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e  # using our custom exception


def save_numpy_array_data(file_path: str, array: np.array):
    """
    save numpy array data to file
    file_path: str location of file to save
    array: np.array data save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise HousingException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data load
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e


def save_object(file_path: str, obj):
    """
    :param file_path: str
    :param obj: any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise HousingException(e, sys) from e


def load_object(file_path: str):
    """
    :param file_path: str
    :return: loaded object
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise HousingException(e, sys) from e


def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(file_path=schema_file_path)  # reads the schema file
        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]  # extract  the columns name and type key/values
        dataframe = pd.read_csv(file_path)
        error_message = ""

        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])  # assigns the datatype to the corresponding column
            else:
                error_message = f"{error_message} \n Column: [{column}] is not in the schema."
            if len(error_message) > 0:
                raise Exception(error_message)
        return dataframe

    except Exception as e:
        raise HousingException(e, sys) from e
