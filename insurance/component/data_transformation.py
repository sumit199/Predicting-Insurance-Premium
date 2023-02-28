from insurance.entity import artifact_entity, config_entity
from insurance.logger import logging
from insurance.exception import InsuranceException
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from insurance import utils
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy import stats
from sklearn.preprocessing import LabelEncoder
from sensor.config import TARGET_COLUMN, OUTLIER_COLUMN, CATEGORICAL_COLUMN

class DataTransformation:

    def __init__(self, data_transformation_config:config_entity.DataTransformationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):

        try:
            logging.info(f"{'>>'*20} Data Transformation {'<<'*20}")
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e, sys)


    def initiate_data_transformation(self):
        
        try:
            #reading training and testing file
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            
            #selecting input feature for train and test dataframe
            input_feature_train_df=train_df.drop(TARGET_COLUMN,axis=1)
            input_feature_test_df=test_df.drop(TARGET_COLUMN,axis=1)

            #selecting target feature for train and test dataframe
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_test_df = test_df[TARGET_COLUMN]

            #removing outlier from train dataset
            z1 = np.abs(stats.zscore(input_feature_train_df[OUTLIER_COLUMN]))
            for i in (np.where(z1>3)):
                input_feature_train_df.drop(i,inplace=True)
            input_feature_train_df.set_index( np.arange(len(input_feature_train_df)),inplace=True )
            
            #removing outlier from train dataset
            z1 = np.abs(stats.zscore(input_feature_test_df[OUTLIER_COLUMN]))
            for i in (np.where(z1>3)):
                input_feature_test_df.drop(i,inplace=True)
            input_feature_test_df.set_index( np.arange(len(input_feature_test_df)),inplace=True )

            #handling categorical column
            label_encoder = LabelEncoder()
            label_encoder.fit_transform(target_feature_train_df[CATEGORICAL_COLUMN])
            label_encoder.fit_transform(target_feature_train_df[CATEGORICAL_COLUMN])

            #transforming input features
            standard_scalar = StandardScaler()
            input_feature_train_arr = standard_scalar.transform(input_feature_train_df)
            input_feature_test_arr = standard_scalar.transform(input_feature_test_df)
