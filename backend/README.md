# Student Dropout Risk Predictor - Backend

This is the **Flask** backend for the Student Dropout Risk Predictor application. It serves a Machine Learning model (Random Forest) to predict student dropout risk based on various demographic and academic factors.

## Tech Stack

- **Framework:** Flask
- **ML Library:** Scikit-learn
- **Data Processing:** Pandas
- **Serialization:** Joblib
- **Server:** Gunicorn (for production)

## Prerequisites

- **Python:** 3.10+
- **pip** (Python package installer)

## Setup & Installation

1.  **Create and Activate a Virtual Environment**:
    It is recommended to run this project in a virtual environment.
    ```bash
    # Create venv
    python3 -m venv venv

    # Activate venv
    # macOS/Linux:
    source venv/bin/activate
    # Windows:
    # venv\Scripts\activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Train the Model**:
    The application requires a trained model artifact (`model_artifacts.joblib`). If this file is missing or you want to retrain the model with new data:
    ```bash
    python train.py
    ```
    *Note: This script expects the training dataset to be located at `../research-space/final-project-data.csv`.*

4.  **Run the Server**:
    ```bash
    python app.py
    ```
    The server will start on `http://127.0.0.1:5000`.

## API Endpoints

### Health Check
- **Endpoint:** `GET /api/health`
- **Description:** Checks if the server is running and the model is loaded.
- **Response:**
  ```json
  {
    "status": "healthy",
    "model_loaded": true
  }
  ```

### Predict Single Student
- **Endpoint:** `POST /api/predict`
- **Description:** Returns a dropout risk prediction for a single student.
- **Body:** JSON object containing feature values (e.g., `{"Marital status": 1, "Course": 33, ...}`).
- **Response:** JSON object with risk score/label.

### Predict Batch (File)
- **Endpoint:** `POST /api/predict-file` (Implemented via `predict_single` logic or separate handler in `app.py`)
- **Description:** Accepts a CSV file for batch processing.
- **Body:** `multipart/form-data` with key `file`.
- **Response:** JSON object containing predictions for each row.

## Deployment

This app is configured for deployment on platforms like **Render** or **Heroku**.
- **Procfile:** Defines the entry point (`gunicorn -w 2 -b 0.0.0.0:$PORT app:app`).
- **render.yaml:** Configuration for Render deployment.
