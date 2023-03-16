from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.predictor import ModelResolver
import pandas as pd
from insurance.utils import load_object
import os,sys
from datetime import datetime
from insurance.config import CATEGORICAL_COLUMN, TARGET_COLUMN
PREDICTION_DIR="prediction"
    
import numpy as np
def start_batch_prediction(input_file_path):
    try:
        os.makedirs(PREDICTION_DIR,exist_ok=True)
        logging.info(f"Creating model resolver object")
        model_resolver = ModelResolver(model_registry="saved_models")
        logging.info(f"Reading file :{input_file_path}")
        df = pd.read_csv(input_file_path)
        #validation
        
        logging.info(f"Encoding categorical columns ")
        target_encoder = load_object(file_path=model_resolver.get_latest_target_encoder_path())
        input_feature_test_df = df.drop(TARGET_COLUMN,axis=1)
        input_feature_test_df = target_encoder(df=input_feature_test_df, 
                                CATEGORICAL_COLUMN=CATEGORICAL_COLUMN)

        logging.info(f"Loading transformer to transform dataset")
        transformer = load_object(file_path=model_resolver.get_latest_transformer_path())
        input_arr = transformer.transform(input_feature_test_df)
     
        logging.info(f"Loading model to make prediction")
        model = load_object(file_path=model_resolver.get_latest_model_path())
        prediction = model.predict(input_arr)

        df["prediction"]=prediction

        prediction_file_name = os.path.basename(input_file_path).replace(".csv",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")
        prediction_file_path = os.path.join(PREDICTION_DIR,prediction_file_name)
        df.to_csv(prediction_file_path,index=False,header=True)
        return prediction_file_path
    except Exception as e:
        raise InsuranceException(e, sys)