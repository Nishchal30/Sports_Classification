import os, yaml, base64, json, joblib, sys
from ensure import ensure_annotations
from src.Sports_Classification.logger import logging
from src.Sports_Classification.exception import CustomException
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(yaml_file : Path):
    """
    reads yaml files and returns

    Args:
        yaml_file (str) : yaml file path

    Raise:
        CustomException : if any error occurs

    Returns:
        content : yaml file content
    """

    try:
        with open(yaml_file) as file:
            content = yaml.safe_load(file)
            logging.info("yaml file loaded successsfully")
            return content

    except Exception as e:
        logging.info("Error occured in read_yaml method in utils.py file")
        raise CustomException(e, sys)
    

@staticmethod
def save_model(path : Path, model):
    try:
        model.save(path)
    except Exception as e:
        logging.info("Error occured in save_model method in prepare base model file")
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(directory_path : list, verbose = True):
    """
    Create directories from the list of directories

    Args:
        directory_path (list) : list of path of directories
    """

    for path in directory_path:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logging.info("directories created successfully")



@ensure_annotations
def get_size(file_path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(file_path)/1024)
    return f"~ {size_in_kb} KB"