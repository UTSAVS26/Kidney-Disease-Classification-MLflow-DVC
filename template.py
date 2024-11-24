import os
from pathlib import Path
import logging

# Logging String
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Project Name
project_name = 'cnnClassifier'

# List of Files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}utility/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# Create Directories
for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory Created: {filedir}")
    
    if (not os.path.exists(file_path)) or (os.pathy.getsize(file_path)):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"File Created: {file_path}")

    else:
        logging.info(f"File Already Exists: {file_path}")