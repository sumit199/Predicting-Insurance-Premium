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
            drift_report=dict()

            base_columns = base_df.columns
            current_columns = current_df.columns

            for base_column in base_columns:
                base_data,current_data = base_df[base_column],current_df[base_column]
                #Null hypothesis is that both column data drawn from same distrubtion
                
                logging.info(f"Hypothesis {base_column}: {base_data.dtype}, {current_data.dtype} ")
                same_distribution =ks_2samp(base_data,current_data)

                if same_distribution.pvalue>0.05:
                    #We are accepting null hypothesis
                    drift_report[base_column]={
                        "pvalues":float(same_distribution.pvalue),
                        "same_distribution": True
                    }
                else:
                    drift_report[base_column]={
                        "pvalues":float(same_distribution.pvalue),
                        "same_distribution":False
                    }
                    #different distribution

            self.validation_error[report_key_name]=drift_report
        
        except Exception as e:
            raise InsuranceException(e, sys)

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact :
        try:
            logging.info(f"Reading base dataframe")
            base_df = pd.read_csv(self.data_validation_config.base_file_path)
            logging.info(f"Drop null values colums from base df")
            base_df = self.drop_missing_values_column(
                                    df=base_df,report_key_name="missing_values_within_base_dataset")
            
            logging.info(f"Reading train dataframe")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            logging.info(f"Reading test dataframe")
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            logging.info(f"Drop null values colums from train df")
            train_df = self.drop_missing_values_column(df=train_df)
            logging.info(f"Drop null values colums from test df")
            test_df = self.drop_missing_values_column(df=test_df)

           
            logging.info(f"Is all required columns present in train df")
            train_df_column_status = self.is_required_column_exist(base_df=base_df, 
                                    current_df=train_d,report_key_name="missing_values_within_train_dataset")

            logging.info(f"Is all required columns present in test df")
            test_df_column_status = self.is_required_column_exist(base_df=base_df,
                                         current_df=test_df, report_key_name="missing_values_within_train_dataset")

            if train_df_column_status:
                logging.info(f"As all column are available in train df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=train_df,report_key_name="data_drift_within_train_dataset")
            if test_df_column_status:
                logging.info(f"As all column are available in test df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=test_df,report_key_name="data_drift_within_test_dataset")
        
        except Exception as e:
            raise InsuranceException(e, sys)