from insurance.predictor import ModelResolver
from insurance.entity import config_entity,artifact_entity
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.utils import load_object
import pandas  as pd
import sys,os


class ModelPusher:

    def __init__(self,model_pusher_config = config_entity.ModelPusherConfig,
                data_transformation_artifact = artifact_entity.DataTransformationArtifact,
                model_trainer_artifact = artifact_entity.ModelTrainingArtifact):

                try:
                    logging.info(f"{'>>'*20} Data Transformation {'<<'*20}")
                    self.model_pusher_config=model_pusher_config
                    self.data_transformation_artifact=data_transformation_artifact
                    self.model_trainer_artifact=model_trainer_artifact
                    self.model_resolver = ModelResolver(model_registry=self.model_pusher_config.saved_model_dir)
                except Exception as e:
                    raise InsuranceException(e, sys)
    
    def initiate_model_pusher(self,)->ModelPusherArtifact:
        try:
            pass
        
        except Exception as e:
            raise InsuranceException(e, sys)