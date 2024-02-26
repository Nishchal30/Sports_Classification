from src.Sports_Classification.logger import logging
from src.Sports_Classification.exception import CustomException
import urllib.request as request
from src.Sports_Classification.utils.utils import *
import tensorflow as tf
from src.Sports_Classification.Config.configuration import ModelTrainingConfig

class Model_Training:

    def __init__(self, config : ModelTrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    
    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1/255,
            validation_split = 0.20
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


        if self.config.is_augmented:
            train_datagenertor = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                horizontal_flip = True,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                **datagenerator_kwargs
            )
        
        else:
            train_datagenertor = valid_datagenerator

        self.train_generator = train_datagenertor.flow_from_directory(
            directory = self.config.training_data_path,
            subset = "training",
            shuffle = True,
            **dataflow_kwargs
        )


    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.train_generator.samples // self.train_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs = self.config.epochs,
            steps_per_epoch = self.steps_per_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator,
        )

        save_model(
            path = self.config.trained_model_path,
            model = self.model
        )

