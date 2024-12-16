import os
from subprocess import run

cleaned_pivo_bahia_path = "data/cleaned_pivo_bahia.csv"
cleaned_horta_ufop_path = "data/cleaned_horta_ufop.csv"

def run_preprocessing():
    """
    Run the data preprocessing script if cleaned datasets are missing.
    """
    if not os.path.exists(cleaned_pivo_bahia_path) or not os.path.exists(cleaned_horta_ufop_path):
        print("Preprocessed files not found. Running data preprocessing...")
        run(["python", "scripts/data_preprocessing.py"])
    else:
        print("Preprocessed files found. Skipping data preprocessing.")

def run_model_training_and_evaluation():
    """
    Run the model training and evaluation script.
    """
    print("Running model training and evaluation...")
    run(["python", "scripts/soil_moisture_prediction.py"])

if __name__ == "__main__":
    run_preprocessing()
    run_model_training_and_evaluation()
