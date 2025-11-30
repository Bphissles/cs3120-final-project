# Student Dropout Risk Predictor - Backend

This is the Flask backend for the Student Dropout Risk Predictor application.

## Setup

1.  **Install Dependencies**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Train the Model**:
    Before running the app, you need to train the model to generate the artifacts (`model_artifacts.joblib`).
    ```bash
    python train.py
    ```
    This script looks for the dataset in `../research-space/final-project-data.csv` (or similar paths).

3.  **Run the Server**:
    ```bash
    python app.py
    ```
    The server will start on `http://127.0.0.1:5000`.

## Endpoints

-   `POST /api/predict`: Predict dropout risk for a single student. Expects JSON data.
-   `POST /api/predict-file`: Predict dropout risk for a batch of students. Expects a CSV file upload (key: `file`).
-   `GET /api/health`: Health check.

## Deployment

This app is configured for deployment on Render/Netlify using `gunicorn`.
-   `Procfile` and `render.yaml` are included.
