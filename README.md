# Crop Disease Presence Classifier
Predictive modeling for crop health. This project leverages pest presence and environmental features to detect and classify agricultural diseases.

# Disease Presence Prediction Model

This repository contains a machine learning pipeline designed to predict `Disease_Presence` based on various numerical, categorical, and binary features (including `Pest_Presence`). The script processes agricultural or environmental data, handles missing values, balances classes, and trains a Logistic Regression model.

---

## Overview

The code performs an end-to-end data preparation and modeling workflow:
1.  **Data Ingestion:** Reads data from `dataset.csv`.
2.  **Feature Engineering:** Extracts the day from datetime columns.
3.  **Data Splitting:** Separates the dataset into labeled (for training/testing) and unlabeled sets.
4.  **Preprocessing:** Applies targeted imputation and scaling/encoding based on data types.
5.  **Modeling:** Uses SMOTE to handle class imbalances and trains a Logistic Regression classifier.
6.  **Export:** Saves the trained model as a `.joblib` file for future inference.

---

## Dependencies

Ensure you have the following Python libraries installed before running the script:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `scikit-learn`
* `imbalanced-learn`
* `joblib`

You can install these dependencies using pip:
`pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn joblib`

---

## Dataset Requirements

The script expects a file named `dataset.csv` in the root directory. Key columns expected by the pipeline include:

* **`Disease_Presence`**: The target variable (must contain some missing values which will be separated into an `unlabeled` set).
* **`Pest_Presence`**: Treated as a binary feature.
* **`Date`**: A date string column that will be parsed into datetime objects to extract the `Day`.

---

## Pipeline Architecture

The data transformation and modeling are handled using a robust scikit-learn and imblearn `Pipeline`. 

### Preprocessing Steps

| Feature Type | Pipeline Transformations |
| :--- | :--- |
| **Numeric Features** | Imputation (Median) → Standard Scaler |
| **Categorical Features** | Imputation (Most Frequent) → One-Hot Encoder |
| **Binary Features** | Imputation (Most Frequent) |

### Classification & Balancing

* **SMOTE (Synthetic Minority Over-sampling Technique):** Applied to the training data to generate synthetic samples for the minority class, ensuring the model does not become biased toward the majority class.
* **Logistic Regression:** Configured with `class_weight="balanced"` to further penalize misclassifications of the minority class.

---

## Output

Upon successful execution, the script fits the pipeline to the training data and exports the final model to your local directory:

* **`pest_model.joblib`**: The serialized model pipeline, ready for deployment or inference on the unlabeled dataset.
