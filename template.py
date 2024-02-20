import os
from pathlib import Path

list_of_files=[
    "github/workflows/.gitkeep",
    "src/__init__.py",
    "src/Components/__init__.py",
    "src/Components/data_ingestion.py",
    "src/Components/data_transformation.py",
    "src/Components/model_trainer.py",
    "src/Components/model_eveluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/loger/logging.py"
    "src/exception/exception",
    "test/unit/__init__py",
    "test/integration/__init__py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"

]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
