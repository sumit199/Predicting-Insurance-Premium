import os, sys
import pandas as pd
import numpy as np
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity import config_entity
from insurance.entity import artifact_entity
from insurance import utils
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise IndentationError(e,sys)
    
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            #Exporting collection data as dataframe
            logging.info(f"Exporting collection data as pandas dataframe")
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name, 
                collection_name=self.data_ingestion_config.collection_name)
            
            logging.info("Save data in feature store")
            #save data in datframe file
            logging.info("Create dataframe folder if not available")
            #creating dataframe folder
            dataframe_file_dir=os.path.dirname(self.data_ingestion_config.dataframe_file_path)
            os.makedirs(dataframe_file_dir,exist_ok=True)
            #save df to dataframe folder
            df.to_csv(
                path_or_buf=self.data_ingestion_config.dataframe_file_path,index=False,header=True)

            logging.info("split dataset into train and test set")
            #split dataset into train and test set
            train_df,test_df = train_test_split(
                        df,test_size=self.data_ingestion_config.test_size,random_state=42)

            logging.info("create dataset directory folder if not available")
            #create dataset directory
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)

            logging.info("Save df to feature store folder")
            #save df to feature store folder
            train_df.to_csv(
                path_or_buf=self.data_ingestion_config.train_file_path, index=False,header=True)
            test_df.to_csv(
                path_or_buf=self.data_ingestion_config.test_file_path, index=False,header=True)            

            #prepare artifact
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                 dataframe_file_path=self.data_ingestion_config.dataframe_file_path,
                 train_file_path=self.data_ingestion_config.train_file_path, 
                 test_file_path=self.data_ingestion_config.test_file_path)
            
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise InsuranceException(error_message=e, error_detail=sys)