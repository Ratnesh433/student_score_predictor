# Student Exam Performance Indicator

This project implements an end-to-end machine learning pipeline to predict student mathematics scores based on various demographic and academic factors. It includes data ingestion, data transformation, model training, and a Flask-based web application for making predictions.

## Features

  * **Data Ingestion**: Reads raw data, splits it into training and testing datasets, and saves them along with the raw data into the `artifacts` directory.
  * **Data Transformation**: Preprocesses the numerical features (reading score, writing score) using `StandardScaler` and handles categorical features (gender, race/ethnicity, parental level of education, lunch, test preparation course) using `OneHotEncoder`. The preprocessor is saved for future use.
  * **Model Training**: Trains and evaluates multiple regression models (Random Forest, Decision Tree, Gradient Boosting, Linear Regression, K-Neighbors Regressor, XGBoost, CatBoost, AdaBoost) using GridSearchCV for hyperparameter tuning. The best-performing model is saved.
  * **Model Prediction**: Uses the trained model and preprocessor to predict mathematics scores for new, unseen data points.
  * **Web Application**: A user-friendly web interface built with Flask allows users to input student details and get instant predictions.

## Technologies Used

  * Python
  * pandas
  * numpy
  * scikit-learn
  * catboost
  * xgboost
  * dill
  * Flask
  * seaborn (for potential visualization in notebooks, though not directly used in the app logic)
  * matplotlib (for potential visualization in notebooks)

## Project Structure

```
.
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw.csv
│   ├── test.csv
│   └── train.csv
├── catboost_info/
│   ├── catboost_training.json
│   ├── learn/
│   │   └── events.out.tfevents
│   └── time_left.tsv
├── notebook/
│   └── study.csv
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/
│   ├── home.html
│   └── index.html
├── .DS_Store
├── .gitignore
├── app.py
├── readme.md
├── requirements.txt
└── setup.py
```

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ratnesh433/student_score_predictor.git
    cd student_score_predictor
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

      * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
      * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Prepare Data and Train Model:**
    Before running the web application, you need to ingest the data, perform transformations, and train the machine learning model. This process will generate the necessary `model.pkl` and `preprocessor.pkl` files in the `artifacts` directory.

    ```bash
    python src/components/data_ingestion.py
    ```

    This script will:

      * Read `notebook/study.csv`.
      * Perform a train-test split.
      * Save `raw.csv`, `train.csv`, and `test.csv` to the `artifacts` folder.
      * Initiate data transformation and save `preprocessor.pkl`.
      * Initiate model training and save `model.pkl`.

2.  **Start the Flask Web Application:**
    Once the model and preprocessor files are generated, you can run the Flask application.

    ```bash
    python app.py
    ```

3.  **Access the Application:**
    Open your web browser and navigate to `http://0.0.0.0:3000` (or `http://127.0.0.1:3000`).

      * The home page (`index.html`) will be displayed.
      * Click on "Start Prediction" or navigate to `/predictdata` to go to the prediction page (`home.html`), where you can input student details and get a predicted mathematics score.

## Files Description

  * `app.py`: The main Flask application file that handles web routes and integrates with the prediction pipeline.
  * `requirements.txt`: Lists all Python libraries required for the project.
  * `setup.py`: Setup script for packaging the project.
  * `notebook/study.csv`: The raw dataset used for training and testing the model.
  * `artifacts/model.pkl`: The serialized machine learning model trained on the data.
  * `artifacts/preprocessor.pkl`: The serialized data transformation object used to preprocess new data before prediction.
  * `src/components/data_ingestion.py`: Script responsible for reading the dataset and splitting it into training and testing sets.
  * `src/components/data_transformation.py`: Defines the data transformation steps, including numerical scaling and categorical encoding.
  * `src/components/model_trainer.py`: Contains logic for training various machine learning models, evaluating them, and selecting the best one.
  * `src/pipeline/predict_pipeline.py`: Provides classes to handle custom data input and make predictions using the loaded model and preprocessor.
  * `src/utils.py`: Contains utility functions for saving/loading Python objects and evaluating model performance.
  * `src/logger.py`: Configures logging for the application to track events and errors.
  * `src/exception.py`: Defines a custom exception handling class for better error management.
  * `templates/home.html`: HTML template for the student score prediction input form and displaying results.
  * `templates/index.html`: HTML template for the main landing page of the web application.
  * `catboost_info/`: Contains training logs and information from CatBoost during model training.
  * `.gitignore`: Specifies files and directories to be ignored by Git.