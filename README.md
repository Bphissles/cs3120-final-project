# Student Dropout Risk Predictor
**Revised using Google Gemini 3**

Predict student dropout risk using a supervised Machine Learning model with a **Nuxt.js (Vue 3)** frontend and a **Flask (Python)** backend.

## Overview

- **Goal:** Sort students into risk categories and present ranked results to help identify at-risk students early.
- **Model:** Uses a **Random Forest classifier** to capture non-linear feature interactions and predict outcomes (Dropout, Enrolled, Graduate).
- **Modes:**
    - **Single-student form input:** Interactive web form for individual assessment.
    - **Batch CSV upload:** Process large datasets efficiently with exportable results.

## Dataset

- **Source:** [UCI ML Repository — Predict Students Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
- **Size:** 4,424 rows
- **Features:** 36 total (Demographic, Socio-economic, Macro-economic, Academic)
- **Target:** Dropout, Enrolled, Graduate

## Tech Stack

- **Frontend:** Nuxt.js 3 (Vue, SCSS)
- **Backend:** Flask (Python)
- **ML:** Scikit-learn, Pandas
- **Deployment:** Netlify (Frontend), Render (Backend)

## Project Structure

```
cs3120-final-project/
├─ backend/                # Flask application & ML Model
│  ├─ app.py               # API entry point
│  ├─ model.py             # Prediction logic
│  ├─ train.py             # Training script
│  └─ model_artifacts.joblib # Trained model (generated)
├─ frontend/               # Nuxt.js application
│  ├─ app/                 # Vue components & pages
│  └─ nuxt.config.ts       # Frontend configuration
└─ research-space/         # Dataset & Jupyter notebooks
   └─ final-project-data.csv
```

## Local Development

### Prerequisites
- **Node.js** v22 or higher
- **Python** 3.10+

### Quick Start

1.  **Backend Setup**:
    Navigate to `backend/` and follow the [Backend README](./backend/README.md) to install dependencies and start the Flask server.
    ```bash
    cd backend
    # ... setup instructions ...
    python app.py
    ```

2.  **Frontend Setup**:
    Navigate to `frontend/` and follow the [Frontend README](./frontend/README.md) to install dependencies and start the Nuxt development server.
    ```bash
    cd frontend
    # ... setup instructions ...
    npm run dev
    ```

3.  **Access**:
    Open `http://localhost:3000` in your browser.

## Features Status

- [x] **ML Model:** Trained Random Forest model with ~19 key features.
- [x] **API:** Flask endpoints for single and batch predictions.
- [x] **Frontend:** Responsive UI for data entry and results visualization.
- [x] **Batch Processing:** Upload CSV capability with row-level error reporting.
- [x] **Export:** Download processed results as CSV.

## Deployment

- **Frontend:** Deployed on **Netlify**.
- **Backend:** Deployed on **Render** using Gunicorn.

## Author
Benjamin Hislop (900896194)
