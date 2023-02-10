import os,sys
from datetime import datetime
from insurance.exception import InsuranceException
from insurance.logger import logging

FILE_NAME="insurance.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"

class TrainingPipelineConfig:
   
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact_dir", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise InsuranceException(e,sys)

class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
        
            self.database_name="insurance_dataset"
            self.collection_name="insurance_premium"
            self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion_dir")
            self.dataframe_file_path =os.path.join(self.data_ingestion_dir,"dataframe_file",FILE_NAME)
            self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
        
        except Exception as e:
            raise InsuranceException(e,sys)

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise InsuranceException(e,sys)

class DataValidationConfig:...

class DataTransformationConfig:...

class ModelTrainingConfig:...

class ModelEvaluationConfig:...

class ModelPusherConfig:...
