import os, sys
import pandas as pd
import numpy as np
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity import config_entity
from insurance.entity import artifact_entity
from insurance import utils

class DataIngestion:

    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise IndentationError(e,sys)
    
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact(dataframe_file_path, train_file_path, test_file_path):
        try:
            #Exporting collection data as dataframe
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name, 
                collection_name=self.data_ingestion_config.collection_name)
            
            logging.info("Save data in feature store")
            #save data in datframe file
            logging.info("Create dataframe folder if not available")
            #creating dataframe folder
            dataframe_file_dir=os.path.dirname(self.data_ingestion_config.dataframe_file_path)
            os.mkdir(dataframe_file_dir,exist_ok=True)
            #save df to dataframe folder
            df.to_csv(path_or_buf=self.data_ingestion_config.dataframe_file_path,index=False,header=True)

            logging.info("split dataset into train and test set")
            #split dataset into train and test set
            

        except Exception as e:
            raise IndentationError(e,sys)