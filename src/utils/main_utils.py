import os
import sys
import dill
import yaml
import base64
from src.logger import logging
from src.exception import CustomException


def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise CustomException(e, sys) from e


def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise CustomException(e, sys) from e


def image_to_base64(image):
    try:
        logging.info("Entered the image_to_base64 method of utils")
        with open(image, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())
        logging.info("Exited the image_to_base64 method of utils")
        return my_string
    except Exception as e:
        raise CustomException(e, sys) from e


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e, sys) from e
