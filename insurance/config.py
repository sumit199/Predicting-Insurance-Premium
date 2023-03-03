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
PARAM_ADR = {'n_estimators':[500,1000,2000],
             'learning_rate':[.001,0.005,0.01,.1],
             'random_state':[1]
             }