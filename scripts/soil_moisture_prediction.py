import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

os.makedirs("models", exist_ok=True)
os.makedirs("output", exist_ok=True)

feature_names = [
    "Tensão da Bateria (V)",
    "Temperatura do Circuito Eletrônico (°C)",
    "Temperatura do Solo (°C)",
    "Capacitância (pF)",
    "Permissividade Relativa",
    "Condutividade (µS/cm)",
    "Salinidade (µS/cm)"
]

feature_names_path = "models/feature_names.joblib"
joblib.dump(feature_names, feature_names_path)

report_path = "output/evaluation_report.txt"

with open(report_path, "w") as report_file:
    report_file.write("Evaluation Report:\n")
    report_file.write("=====================\n")

cleaned_files = [f for f in os.listdir("data") if f.startswith("cleaned_") and f.endswith(".csv")]

datasets = {}
models = {}

for file in cleaned_files:
    file_path = os.path.join("data", file)
    print(f"Processing: {file}")
    
    dataset = pd.read_csv(file_path)
    
    def split_dataset(dataset):
        X = dataset[feature_names]
        y = dataset["Umidade (%)"]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    X_train, X_test, y_train, y_test = split_dataset(dataset)

    model = RandomForestRegressor(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)

    model_path = f"models/{file.replace('cleaned_', '').replace('.csv', '_model.joblib')}"
    joblib.dump(model, model_path)

    datasets[file] = (X_test, y_test)
    models[file] = model

    y_pred = model.predict(X_test)
    mse_self = mean_squared_error(y_test, y_pred)

    with open(report_path, "a") as report_file:
        report_file.write(f"Dataset: {file}\n")
        report_file.write(f"MSE on self-dataset: {mse_self}\n\n")

    plot_path = f"output/{file.replace('cleaned_', '').replace('.csv', '_predictions.png')}"
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.6, edgecolor='k', label="Valores previstos")
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--',
        linewidth=2,
        label="Valores reais (linha y=x)"
    )
    plt.xlabel("Valores Reais (Umidade %)")
    plt.ylabel("Valores Previstos (Umidade %)")
    plt.title(f"{file}: True vs Predicted")
    plt.legend(loc="upper left")
    plt.grid()
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to {plot_path}")

with open(report_path, "a") as report_file:
    report_file.write("Cross-Dataset Evaluation:\n")
    report_file.write("===========================\n")

for train_file, model in models.items():
    for test_file, (X_test, y_test) in datasets.items():
        if train_file != test_file:  # Skip self-evaluation
            y_pred_cross = model.predict(X_test)
            mse_cross = mean_squared_error(y_test, y_pred_cross)

            with open(report_path, "a") as report_file:
                report_file.write(f"Model trained on {train_file}, tested on {test_file}:\n")
                report_file.write(f"MSE: {mse_cross}\n\n")

print(f"Evaluation report saved to {report_path}")
