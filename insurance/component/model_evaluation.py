from insurance.predictor import ModelResolver
from insurance.entity import config_entity,artifact_entity
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.utils import load_object
from sklearn.metrics import f1_score
import pandas  as pd
import sys,os
from insurance.config import TARGET_COLUMN, CATEGORICAL_COLUMN

class ModelEvaluation:
    def __init__(self,
        model_eval_config:config_entity.ModelEvaluationConfig,
        data_ingestion_artifact:artifact_entity.DataIngestionArtifact,
        data_transformation_artifact:artifact_entity.DataTransformationArtifact,
        model_trainer_artifact:artifact_entity.ModelTrainingArtifact     
        ):
        try:
            logging.info(f"{'>>'*20}  Model Evaluation {'<<'*20}")
            self.model_eval_config=model_eval_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_transformation_artifact=data_transformation_artifact
            self.model_trainer_artifact=model_trainer_artifact
            self.model_resolver = ModelResolver()
        except Exception as e:
            raise InsuranceException(e,sys)

    def initiate_model_evaluation(self):

        try:
            pass
        except Exception as e:
            raise InsuranceException(e, sys)