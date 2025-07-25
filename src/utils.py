import os
import sys
import numpy as np
import pandas as pd
import dill 

from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV

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
    
def evaluate_models(X_train,y_train,X_test,y_test,models,params,cv=3,n_jobs=3,verbose=1,refit=False):
    try:
        report={}
        for i in range(len(models)):
            
            model=list(models.values())[i]
            para=params[list(models.keys())[i]]
            
            gs = GridSearchCV(model,para,cv=cv,n_jobs=n_jobs,verbose=verbose,refit=refit)
            gs.fit(X_train,y_train)
            
            
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            
            train_model_score=r2_score(y_train, y_train_pred)
            test_model_score=r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]]=test_model_score
     

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path: str):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
