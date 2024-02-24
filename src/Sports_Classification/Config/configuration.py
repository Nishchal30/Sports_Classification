from src.Sports_Classification.Constants import *
from src.Sports_Classification.utils.utils import read_yaml, create_directories
from src.Sports_Classification.Entity.config_entity import DataIngestionConfig, BaseModelConfig


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