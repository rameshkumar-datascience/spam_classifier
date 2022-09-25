import os
from pathlib import Path

package_name = "spam_classifier"

list_of_files = [
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py",
   f"src/{package_name}/exception/__init__.py",
   f"src/{package_name}/logger/__init__.py", 
   f"src/{package_name}/components/__init__.py",
   f"src/{package_name}/components/text_preprocessing.py",
   f"src/{package_name}/components/data_transformation.py",
   f"src/{package_name}/components/model_training.py",
   f"src/{package_name}/components/model_evaluation.py",
   f"src/{package_name}/components/model_pusher.py",
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "dvc.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print("Directory created")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            print("Created an empty file")

    else:
        print("File already exists")