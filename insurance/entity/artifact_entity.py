from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    dataframe_file_path:str
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str
    

class DataTransformationArtifact:...

class ModelTrainingArtifact:...

class ModelEvaluationArtifact:...

class ModelPusherArtifact:...
