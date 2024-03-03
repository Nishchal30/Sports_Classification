import mlflow
import mlflow.keras
from urllib.parse import urlparse
import tensorflow as tf
from pathlib import Path
from src.Sports_Classification.utils.utils import save_json
from src.Sports_Classification.Config.configuration import ModelEvaluationConfig


class Model_Evaluation:

    def __init__(self, config : ModelEvaluationConfig):
        self.config = config

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1/255,
            validation_split = 0.2
        )

        dataflow_kwargs = dict(
            target_size = self.config.image_size[:-1],
            batch_size = self.config.batch_size,
            interpolation = "bilinear"
        )


        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )


        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data_path,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(model_path : Path) -> tf.keras.Model:
        return tf.keras.models.load_model(model_path)
    

    def eveluate_model(self):
        self.model = self.load_model(self.config.model_path)
        self.train_valid_generator()
        self.score = self.model.evaluate(self.valid_generator)

    def save_score(self):
        scores = {"loss" : self.score[0], "accuracy" : self.score[1]}
        save_json(path = Path("model_score.json"), data = scores)



    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss" : self.score[0], "accuracy" : self.score[1]})

            
            if tracking_url != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16")
            else:
                mlflow.keras.log_model(self.model,"model")