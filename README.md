# Student Performance Predictor

## Project Overview

This project predicts whether a student will pass or fail based on academic and demographic features.

## Dataset

The project uses the UCI Student Performance Dataset.

Features include:

* Study time
* Number of past failures
* Absences
* Mother's education level
* Father's education level

## Machine Learning Model

* Logistic Regression
* Train/Test Split
* Performance Evaluation using:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

## Results

### Model with G1 and G2

Accuracy: 88.6%

### Model without G1 and G2

Accuracy: 74.7%

This experiment demonstrates the effect of feature leakage and the importance of proper feature selection.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook
* Git & GitHub
## Project Structure

```text
01-student-performance-predictor
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
├── data/
├── notebooks/
└── src/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SariyaQ/student-performance-predictor.git
cd student-performance-predictor
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Machine Learning Workflow

1. Load and explore the dataset.
2. Perform data cleaning and analysis.
3. Create the target variable (`passed`).
4. Train and evaluate machine learning models.
5. Compare Logistic Regression, Decision Tree, and Random Forest.
6. Analyze feature importance.
7. Save the trained model using Joblib.
8. Build an interactive Streamlit application.

## Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 74.7%    |
| Decision Tree       | 64.6%    |
| Random Forest       | 60.8%    |

Feature importance analysis showed that student absences, previous failures, and study time were among the most influential factors affecting academic success.

## Features

* Student performance prediction
* Exploratory Data Analysis (EDA)
* Logistic Regression model
* Decision Tree model
* Random Forest model
* Feature importance analysis
* Interactive Streamlit interface
* Git and GitHub version control

## Future Improvements

* Hyperparameter tuning
* Additional machine learning algorithms
* Cloud deployment
* AI-powered educational recommendations
* Explainable AI visualizations

```
```

## Author

Sariya Gasimova
