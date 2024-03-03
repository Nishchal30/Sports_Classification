from src.Sports_Classification.Components.data_ingestion import DataIngestion
from src.Sports_Classification.Components.prepare_base_model import PrepareBaseModel
from src.Sports_Classification.Components.model_trainer import Model_Training
from src.Sports_Classification.Config.configuration import ConfigurationManager
from src.Sports_Classification.Components.model_evaluation import Model_Evaluation
from src.Sports_Classification.logger import logging




class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()

        logging.info("Data ingestion stage started")

        # Data ingestion 
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip_file()

        logging.info("data ingestion completed")

        # Prepare base model
        base_model_config = config.get_base_model()
        create_base_model = PrepareBaseModel(config=base_model_config)
        create_base_model.create_base_model()
        create_base_model.update_base_model()

        logging.info("preparing base model completed")
        # Model Training

        model_training_config = config.get_model_training_config()
        model_training = Model_Training(config=model_training_config)
        model_training.get_base_model()
        model_training.train_valid_generator()
        model_training.train()

        logging.info("model training completed")

        # Model Evaluation

        eval_config = config.get_evaluation_config()
        evaluation = Model_Evaluation(eval_config)
        evaluation.eveluate_model()
        evaluation.log_into_mlflow()

        logging.info("model evalutaion completed")
if __name__ == '__main__':
    try:
        # logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        # logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e




