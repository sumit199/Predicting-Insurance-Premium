import pymongo
import pandas as pd
import json
from dataclasses import dataclass

# Provide the mongodb localhost url to connect python to mongodb.
import os
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "expenses"
OUTLIER_COLUMN = "bmi"
CATEGORICAL_COLUMN = ["sex","smoker","region"]
PARAM_XGB = {
            'n_estimators':[500],
            'min_child_weight':[4,5], 
            'gamma':[i/10.0 for i in range(3,6)],  
            'subsample':[i/10.0 for i in range(6,11)],
            'colsample_bytree':[i/10.0 for i in range(6,11)], 
            'max_depth': [2,3,4,6,7],
            'objective': ['reg:squarederror', 'reg:tweedie'],
            'booster': ['gbtree', 'gblinear'],
            'eval_metric': ['rmse'],
            'eta': [i/10.0 for i in range(3,6)],
            }