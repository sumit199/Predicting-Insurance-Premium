from insurance.entity import artifact_entity
from insurance.entity import config_entity
from insurance.exception import InsuranceException
from insurance.logger import logging
from scipy.stats import ks_2samp
import pandas as pd
from typing import Optional
import os
import sys



class DataValidation:

    def __init__(self, 
                data_validation_config: config_entity.DataValidationConfig,
                data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.validation_error=dict()
        except Exception as e:
            raise InsuranceException(e, sys)

   

    def drop_missing_values_column(self,df:pd.DataFrame,report_key_name:str)->Optional[pd.DataFrame]:
        """
        This function drop column which contains missing 
        values more than specific threshold

        df: accepts a pandas dataframe
        threshold: percentage criteria to drop a column
        =============================================================================
        returns  pandas Dataframe if atleast single column available after 
        missing columns drop else none
        """
        try:
            
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isnull().sum()/df.shape[0]
            #selecting column name which contains null
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report>threshold].index

            logging.info(f"Columns to drop: {list(drop_column_names)}")
            self.validation_error[report_key_name]=list(drop_column_names)
            df.drop(list(drop_column_names),axis=1,inplace=True)

            #return None no columns left
            if len(df.columns)==0:
                return None

            return df
        except Exception as e:
            raise SensorException(e, sys)

    def is_required_column_exist(self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str)->bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns

            missing_columns = []
            for base_column in base_columns:
                if base_column not in current_columns:
                    logging.info(f"Column: [{base} is not available.]")
                    missing_columns.append(base_column)

            if len(missing_columns)>0:
                self.validation_error[report_key_name]=missing_columns
                return False
            return True
        except Exception as e:
            raise InsuranceException(e, sys)

    def data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str):
        try:
            pass
        
        except Exception as e:
            raise InsuranceException(e, sys)

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact :
        pass