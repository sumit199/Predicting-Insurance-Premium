from insurance.pipeline.training_pipeline import start_training_pipeline
from insurance.pipeline.batch_preediction import start_batch_prediction
filepath = "/config/workspace/insurance.csv"

if __name__=="__main__":

    try:
        #start_training_pipeline()
        output = start_batch_prediction(input_file_path=filepath)
        print(output)

    except Exception as e:
        print(e)