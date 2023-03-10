from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    dataframe_file_path:str
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str
    
@dataclass
class DataTransformationArtifact:
    transformed_test_path:str
    transformed_train_path:str
    transform_object_path:str
    target_encoder_path:str
    
@dataclass
class ModelTrainingArtifact:
    model_path:str
    r2_score_train:str
    r2_score_test:str
    
@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    improved_accuracy:float

class ModelPusherArtifact:...
