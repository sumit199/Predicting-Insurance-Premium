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
    pass