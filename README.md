# Student Dropout Risk Predictor

Predict student dropout risk using a supervised ML model with a Nuxt.js frontend and a Flask backend.

## Overview
- **Goal:** Sort students into risk categories and present ranked results.
- **Model:** Initial approach uses a Random Forest classifier to capture non-linear feature interactions.
- **Modes:** Single-student form input or batch CSV upload. Results exportable as CSV.

## Dataset
- **Source:** UCI ML Repository — Predict Students Dropout and Academic Success
  - https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success
- **Rows:** 4,424
- **Features:** 36 total, ~19 preliminarily relevant
- **Type:** Tabular

Example features: Marital status, Course, Previous qualification, GDP, Daytime/evening attendance, Mother’s qualification, Target, International, Nationality, Father’s qualification, Displaced, Unemployment rate, Educational special needs, Debtor, Gender, Inflation rate, Tuition fees up to date, Scholarship holder, Age at enrollment.

## Features
- **Form processing:** Single-student input with client-side validation.
- **CSV processing:** Batch upload; per-row error reporting with guidance.
- **Results:** Sorted by predicted dropout risk (highest first); optional pie chart.
- **Export:** Download processed results as CSV.

## Tech Stack
- **Frontend:** Nuxt.js (Vue, HTML, CSS, JS)
- **Backend:** Flask
- **SSR/Process Manager:** pm2
- **Hosting:** Netlify (frontend), Render (backend)

## Project Structure
```
cs3120-final-project/
├─ frontend/
│  └─ app/
│     ├─ pages/
│     │  ├─ index.vue
│     │  └─ about.vue
│     └─ app.vue
└─ backend/
```

## Local Development

### Prerequisites
- Node.js 18+
- pnpm or npm
- Python 3.10+
- pip / venv

### Frontend (Nuxt)
```
# from frontend/app
pnpm install        # or: npm install
pnpm dev            # or: npm run dev
```
Dev server will run at http://localhost:3000 by default.

### Backend (Flask)
- TODO: Initialize Flask app in `backend/`.
- TODO: Provide `/predict` endpoint for single prediction.
- TODO: Provide `/predict-batch` endpoint for CSV file upload.
- TODO: Package model artifact(s) and preprocessor(s).
- TODO: Add CORS configuration for the Nuxt dev origin.

Suggested skeleton: - **AI Provided**
```
backend/
├─ app.py                # Flask app factory and route registration
├─ requirements.txt      # pinned dependencies
├─ model/
│  ├─ train.py           # offline training script (optional)
│  ├─ pipeline.pkl       # serialized model & preprocessors (after training)
│  └─ schema.json        # expected feature schema
└─ routes/
   └─ predict.py         # /predict and /predict-batch handlers
```

## API (Planned)
- POST `/predict`
  - body: JSON with feature values for one student
  - returns: `{ risk: number | string, probabilities?: object }`
- POST `/predict-batch`
  - body: multipart/form-data with `file` (CSV)
  - returns: `{ rows: Array<{ index: number, risk: number | string, errors?: string[] }> }`

Notes:
- Map model outputs to labels (e.g., Low/Medium/High) consistently on backend.
- Return row-level validation errors for batch processing.

## CSV Template (Planned)
- TODO: Provide `frontend/public/template.csv` with required headers.
- TODO: Document schema and allowed values in backend `schema.json` and README.

## Deployment
- Frontend: Netlify
  - Build command: `npm build`
  - Publish directory: `.output/public` (Nuxt static) or SSR with adapter as needed
- Backend: Render (Flask)
  - Gunicorn entrypoint: `gunicorn -w 2 -b 0.0.0.0:$PORT app:app`
  - Set environment variables securely

## Development Notes
- Prefer simple, well-documented code. Add clear comments for business logic and model pipelines.
- Handle environments (dev/prod) carefully. Do not overwrite `.env` files.
- No mocks in dev/prod. Use mocks only for tests.

## Author
Benjamin Hislop (900896194)
