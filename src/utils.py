import os
import sys
import numpy as np
import pandas as pd
import dill 

from src.exception import CustomException


def save_object(file_path: str, obj: object):
    """
    Saves an object to a file using dill serialization.
    
    Parameters:
    - file_path (str): The path where the object will be saved.
    - obj (object): The object to be saved.
    
    Raises:
    - CustomException: If there is an error during the saving process.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        print(f"Object saved successfully at {file_path}")
    except Exception as e:
        raise CustomException(e, sys)