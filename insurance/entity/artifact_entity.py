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
    
class ModelTrainingArtifact:...

class ModelEvaluationArtifact:...

class ModelPusherArtifact:...
