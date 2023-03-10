from insurance.entity import artifact_entity, config_entity
from insurance.logger import logging
from insurance.exception import InsuranceException
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from insurance import utils
import numpy as np
from sklearn.preprocessing import RobustScaler
from scipy import stats
from insurance.config import TARGET_COLUMN, OUTLIER_COLUMN, CATEGORICAL_COLUMN

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

            logging.info("handling categorical columns")
            #handling categorical column
            input_feature_train_df = utils.encoder(df=input_feature_train_df, 
                                CATEGORICAL_COLUMN=CATEGORICAL_COLUMN)

            input_feature_test_df = utils.encoder(df=input_feature_test_df, 
                                CATEGORICAL_COLUMN=CATEGORICAL_COLUMN)
            
            #transforming input features
            robust_scalar = RobustScaler()
            input_feature_train_arr = robust_scalar.fit_transform(input_feature_train_df)
            input_feature_test_arr = robust_scalar.transform(input_feature_test_df)

            #target encoder
            train_arr = np.c_[input_feature_train_arr, target_feature_train_df]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_df]

            #save numpy array
            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_train_path,
                                        array=train_arr)

            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_test_path,
                                        array=test_arr)

            
            utils.save_object(file_path=self.data_transformation_config.transform_object_path,
             obj=robust_scalar)

            utils.save_object(file_path=self.data_transformation_config.target_encoder_path,
            obj=utils.encoder)


            data_transformation_artifact = artifact_entity.DataTransformationArtifact(
                transformed_train_path = self.data_transformation_config.transformed_train_path,
                transformed_test_path = self.data_transformation_config.transformed_test_path,
                 transform_object_path=self.data_transformation_config.transform_object_path,
                target_encoder_path = self.data_transformation_config.target_encoder_path

            )

            logging.info(f"Data transformation object {data_transformation_artifact}")
            return data_transformation_artifact


        except Exception as e:
            raise InsuranceException(e, sys)