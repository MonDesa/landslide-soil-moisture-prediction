# landslide-soil-moisture-prediction

This project focuses on developing predictive models for soil moisture using real-world data collected from monitoring stations. The analysis leverages the **Random Forest Regressor** to predict soil moisture based on a set of environmental and sensor-related features. The workflow includes data preprocessing, model training, self-evaluation, and cross-dataset evaluation to highlight the importance of regional soil analysis.

#### **Used Model**
The **Random Forest Regressor** was chosen due to its robustness in handling:
- **Non-linear relationships** between features and target variables.
- **Heterogeneous datasets**, such as those obtained from various soil monitoring stations.
- **Overfitting reduction**, achieved through the aggregation of multiple decision trees, making it a reliable choice for this prediction task.

Additionally, the model provides insights into the importance of each feature, allowing further understanding of the factors influencing soil moisture.

#### **Real Data and Confidentiality**
The data used for training and evaluating the predictive models were **real data**, captured by monitoring stations provided by a manufacturer.  
These data were made available under a confidentiality agreement, preventing their complete disclosure. However, the manufacturer has expressed interest in publishing the study results in the future.  
This collaboration ensures the practical applicability of the developed models and promotes advancements in soil moisture analysis.

## Running environment guide:

### **1. Build the Docker Image**
Navigate to the directory containing `Dockerfile` and run:
```bash
docker build -t soil-moisture-env .
```

This creates a Docker image named `soil-moisture-env`.

---

### **2. Run the Docker Container**
Run the container, mounting project directory:
```bash
docker run -it --rm -v $(pwd):/app soil-moisture-env
```

- **`-it`**: Interactive mode.
- **`--rm`**: Automatically remove the container after exit.
- **`-v $(pwd):/app`**: Mounts current directory (`$(pwd)`) to `/app` in the container.

---

### **3. Run the Script**
Execute the script using Python:
```bash
python main.py
```

---

### **4. Check Results**
- The output will display MSE values for both self and cross-dataset evaluations.
- Models will be saved to the `/app/models` directory in the container, which is mapped to local `models/` folder.

---