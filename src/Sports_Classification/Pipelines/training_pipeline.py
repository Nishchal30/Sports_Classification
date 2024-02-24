from src.Sports_Classification.Components.data_ingestion import DataIngestion
from src.Sports_Classification.Components.prepare_base_model import PrepareBaseModel
from src.Sports_Classification.Config.configuration import ConfigurationManager


config = ConfigurationManager()

# Data ingestion 
data_ingestion_config = config.get_data_ingestion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.extract_zip_file()

# Prepare base model
base_model_config = config.get_base_model()
create_base_model = PrepareBaseModel(config=base_model_config)
create_base_model.create_base_model()
create_base_model.update_base_model()

