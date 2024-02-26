import os
from dataclasses import dataclass
from pathlib import Path

# Data Ingestion Config

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_path : Path
    local_data_file : Path
    unzip_dir : Path


# Prepare pre-trained Model config

@dataclass(frozen=True)
class BaseModelConfig:
    root_dir : Path
    base_model_path : Path
    updated_base_model_path : Path
    image_size_params : list
    learning_rate_params : float
    include_top_params : bool
    weight_params : str
    classes_params : int


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir : Path
    trained_model_path : Path
    updated_base_model_path : Path
    training_data_path : list
    epochs : int
    batch_size : int
    is_augmented : bool
    image_size : list