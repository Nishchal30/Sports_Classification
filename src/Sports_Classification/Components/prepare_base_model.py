from src.Sports_Classification.logger import logging
from src.Sports_Classification.exception import CustomException
from src.Sports_Classification.utils.utils import *
import tensorflow as tf
from src.Sports_Classification.Config.configuration import BaseModelConfig


class PrepareBaseModel:

    logging.info("Preparing base model...")

    def __init__(self, config : BaseModelConfig):
        self.config = config

    def create_base_model(self):
        try:
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape = self.config.image_size_params,
                weights = self.config.weight_params,
                include_top = self.config.include_top_params
            )

            self.save_model(path = self.config.base_model_path, model = self.model)
            logging.info(f"Base model which is {self.model} saved at {self.config.base_model_path}")

        except Exception as e:
            logging.info("Error occured in create base model method in prepare base model file")
            raise CustomException(e, sys)


    @staticmethod
    def save_model(path : Path, model):
        try:
            model.save(path)
        except Exception as e:
            logging.info("Error occured in save_model method in prepare base model file")
            raise CustomException(e, sys)
        
        
    @staticmethod
    def create_full_model(learning_rate, freeze_all, freeze_till, classes, model):

        try:
            if freeze_all is not None:
                for layer in model.layers:
                    model.trainable = False
            
            elif (freeze_till is not None) and (freeze_till > 0):
                for layer in model.layers[:freeze_till]:
                    model.trainable = False

            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                            units=classes,
                            activation="softmax"
                        )(flatten_in)

            full_model = tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction
            )

            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )

            full_model.summary()
            logging.info(f"the model is created with summary {full_model.summary()}")

            return full_model
        
        except Exception as e:
            logging.info("Error occured in create full model method in prepare base model file")
            raise CustomException(e, sys)
    

    def update_base_model(self):
        
        try:
            self.full_model = self.create_full_model(
                model=self.model,
                classes=self.config.classes_params,
                freeze_all=True,
                freeze_till=True,
                learning_rate=self.config.learning_rate_params
            )

            self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

            logging.info(f"The updated model saved at {self.config.updated_base_model_path}")
        
        except Exception as e:
            logging.info("Error occured in update base model method in prepare base model file")
            raise CustomException(e, sys)
