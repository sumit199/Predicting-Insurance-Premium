import os, sys
import pandas as pd
import numpy as np
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity import config_entity
from insurance.entity import artifact_entity
from insurance import utils
from xgboost import XGBRegressor
from insurance.config import PARAM_XGB


class ModelTrainer:

    def __init__(self, model_trainer_config:config_entity.ModelTrainingConfig,
                 data_transformer_config:artifact_entity.DataTransformationArtifact):
        try:
            logging.info(f"{'>>'*20} Model Trainer {'<<'*20}")
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact

        except Exception as e:
            raise InsuranceException(e, sys)

    #training model            
    def train_model(self,X,y):
        try:
            xgb_regressor = XGBRegressor()
            xgb_regressor.fit(X,y)
            return xgb_regressor
        except Exception as e:
            raise InsuranceException(e, sys)

    #fine tune model
    def fine_tune(self,X,y):
        try:
            xgb = XGBRegressor()
            n_iter_search = 100
            xgb_random = RandomizedSearchCV(estimator= xgb, param_distributions=PARAM_XGB,
                        n_iter=n_iter_search, cv=5)
            xgb_random.fit(X_train, y_train)
            return xgb_random.best_score_,xgb_random.best_params_           

        except Exception as e:
            raise SensorException(e, sys)


    def initiate_model_trainer(self) -> artifact_entity.ModelTrainingArtifact:
        try:
            
            logging.info(f"Loading train and test array.")
            train_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr = utils.load_numpy_array_data(file_path=self.data_transformation-artifact.transformed_test_path)
            
            logging.info(f"Splitting input and target feature from both train and test arr.")
            x_train,y_train = train_arr[:,:-1],train_arr[:,-1]
            x_test,y_test = test_arr[:,:-1],test_arr[:,-1]

            logging.info(f"Train the model")
            model = self.train_model(X=x_train,y=y_train)

            logging.info(f"Calculating r2 train score")
            y_train_pred = model.predict(x_train)
            r2_score_train = r2_score(y_true=y_train, y_pred=y_train_pred)
            
            logging.info(f"calculating r2 test score")
            y_test_pred = model.predict(y_test)
            r2_score_test = r2_score(y_true=y_test, y_pred=y_test_pred)

            logging.info(f"train score:{r2_score_train} and tests score {r2_score_test}")
            #check for overfitiing or underfitting or expected score
            logging.info(f"Checking if our model is underfitting or not")
            if r2_score_test<self.model_trainer_config.expected_score:
                raise Exception(f"Model is not good as it is not able to give \
                expected accuracy: {self.model_trainer_config.expected_score}: \
                model actual score: {r2_score_test}")

            logging.info(f"Checking if our model is overfitting or not")
            diff = abs(r2_score_train-r2_score_test)

            if diff>self.model_trainer_config.overfitting_threshold:
                raise Exception(f"Train and test score diff: {diff} \
                is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")

             #save the trained model
            logging.info(f"Saving mode object")
            utils.save_object(file_path=self.model_trainer_config.model_path, obj=model)

            #prepare artifact
            logging.info(f"Prepare the artifact")
            model_trainer_artifact  = artifact_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path, 
            r2_score_train=r2_score_train, r2_score_test=r2_score_test)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise SensorException(e, sys)
            