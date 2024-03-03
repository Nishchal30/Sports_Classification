from src.Sports_Classification.Constants import *
import os
from src.Sports_Classification.utils.utils import read_yaml, create_directories
from src.Sports_Classification.Entity.config_entity import DataIngestionConfig, BaseModelConfig,  \
ModelTrainingConfig, ModelEvaluationConfig


class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH
            ):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config["artifacts_root"]])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']

        create_directories([self.config['data_ingestion']['root_dir']])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_path=config['source_path'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )

        return data_ingestion_config
    

    def get_base_model(self) -> BaseModelConfig:
        config = self.config['base_model']

        create_directories([self.config['base_model']['root_dir']])

        base_model_config = BaseModelConfig(
            root_dir = Path(config['root_dir']),
            base_model_path = Path(config['base_model_path']),
            updated_base_model_path = Path(config['updated_base_model_path']),
            image_size_params = self.params['IMAGE_SIZE'],
            learning_rate_params = self.params['LEARNING_RATE'],
            include_top_params = self.params['INCLUDE_TOP'],
            weight_params = self.params['WEIGHTS'],
            classes_params = self.params['CLASSES'] 
            )

        return base_model_config


    def get_model_training_config(self) -> ModelTrainingConfig:
        training = self.config['training']
        prepare_base_model = self.config['base_model']
        params = self.params
        training_data = os.path.join(self.config['data_ingestion']['unzip_dir'], "data/train")

        create_directories([Path(training['root_dir'])])

        training_config = ModelTrainingConfig(
            root_dir = Path(training['root_dir']),
            trained_model_path = Path(training['trained_model_path']),
            updated_base_model_path = Path(prepare_base_model['updated_base_model_path']),
            training_data_path = Path(training_data),
            epochs = params['EPOCHS'],
            batch_size = params['BATCH_SIZE'],
            is_augmented = params['AUGMENTATION'],
            image_size = params['IMAGE_SIZE']
        )


        return training_config
    

    def get_evaluation_config(self) -> ModelEvaluationConfig:
        eval_config = ModelEvaluationConfig(
            model_path =r"D:\Deep_Learning_Projects\Sports_Classification\artifacts\model_training\model.h5",
            training_data_path=r"D:\Deep_Learning_Projects\Sports_Classification\artifacts\data_ingestion\data\train",
            all_params=self.params,
            mlflow_url="https://dagshub.com/Nishchal30/Sports_Classification.mlflow",
            image_size=self.params["IMAGE_SIZE"],
            batch_size=self.params["BATCH_SIZE"],
        )

        return eval_config