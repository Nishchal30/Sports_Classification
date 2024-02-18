import os 
from pathlib import Path

project_name = "Sports_Classification"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/Components/__init__.py",
    f"src/Components/data_ingestion.py",
    f"src/Components/data_transformation.py",
    f"src/Components/model_trainer.py",
    f"src/Pipelines/__init__.py",
    f"src/Pipelines/training_pipeline.py",
    f"src/Pipelines/prediction_pipeline.py",
    f"src/logger.py",
    f"src/exception.py",
    f"src/utils/__init__.py",
    f"src/utils/utils.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py"
]


for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not(os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass

    else:
        print("File already exists")