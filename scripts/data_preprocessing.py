import pandas as pd

def clean_dataset_and_save(input_path, output_path):
    """
    Cleans a dataset and saves it to a new file.
    
    Parameters:
        input_path (str): Path to the raw dataset.
        output_path (str): Path to save the cleaned dataset.
    """
    dataset = pd.read_csv(input_path, delimiter=';', decimal=',')
    
    dataset = dataset.dropna()
    
    numeric_columns = [
        "Tensão da Bateria (V)",
        "Temperatura do Circuito Eletrônico (°C)",
        "Temperatura do Solo (°C)",
        "Capacitância (pF)",
        "Permissividade Relativa",
        "Condutividade (µS/cm)",
        "Salinidade (µS/cm)",
        "Umidade (%)"
    ]
    
    for col in numeric_columns:
        dataset[col] = pd.to_numeric(dataset[col], errors='coerce')
    
    dataset = dataset.dropna()
    
    dataset.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {output_path}")

clean_dataset_and_save("data/pivo_bahia.csv", "data/cleaned_pivo_bahia.csv")
clean_dataset_and_save("data/horta_ufop.csv", "data/cleaned_horta_ufop.csv")
