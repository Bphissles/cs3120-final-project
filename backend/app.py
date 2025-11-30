from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os
from model import DropoutPredictor
import io

app = Flask(__name__)
# Configure CORS to allow specific origins
# Replace with your actual frontend URLs
allowed_origins = [
    "http://localhost:3000",
    "https://www.benhislop.com",
    "https://cs3120-final-project.netlify.app"
]
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

# Initialize predictor
predictor = DropoutPredictor()
# Get directory of current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model_artifacts.joblib")

def load_model():
    if os.path.exists(MODEL_PATH):
        print("Loading model artifacts...")
        predictor.load(MODEL_PATH)
        print("Model loaded.")
    else:
        print("Model artifacts not found. Please run train.py first.")

load_model()

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "model_loaded": predictor.model is not None})

@app.route('/api/predict', methods=['POST'])
def predict_single():
    if predictor.model is None:
        return jsonify({"error": "Model not loaded"}), 503
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        # If data is a single dict, wrap in list
        if isinstance(data, dict):
            data = [data]
            
        results = predictor.predict(data)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/predict-file', methods=['POST'])
def predict_file():
    if predictor.model is None:
        return jsonify({"error": "Model not loaded"}), 503
        
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
        
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "File must be a CSV"}), 400
        
    try:
        # Read CSV
        # Note: The proposal mentions semicolon separator for the source data, 
        # but user uploads might be comma or semicolon. Let's try to detect or assume comma for standard CSVs
        # usually, but the project data uses semicolon.
        # I will try reading with pandas default (comma) first, if that fails (1 col), try semicolon.
        
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        # Reset stream position
        stream.seek(0)
        
        # Try sniffing
        try:
            dialect = pd.read_csv(stream, nrows=5).shape[1]
            stream.seek(0)
            if dialect == 1:
                 df = pd.read_csv(stream, sep=';')
            else:
                 stream.seek(0)
                 df = pd.read_csv(stream)
        except:
            stream.seek(0)
            df = pd.read_csv(stream, sep=';') # Fallback to project default

        results = predictor.predict(df)
        
        # Combine results with original data for the response?
        # Or just return results. The proposal says "output a list of students and their predicted dropout risk".
        # It's helpful to return enough info to identify the student.
        
        response_data = []
        for i, res in enumerate(results):
            row_data = df.iloc[i].to_dict()
            # Add prediction info
            row_data.update(res)
            response_data.append(row_data)
            
        # Sort by confidence of "Dropout" if possible?
        # The proposal says "sorted by predicted dropout risk"
        # "Dropout" is a class label. I need to look at probabilities["Dropout"]
        
        # Filter for valid results that have probabilities
        valid_results = [r for r in response_data if 'probabilities' in r]
        
        # Sort desc by Dropout probability if it exists as a class
        # Check if Dropout is a key in probabilities
        if valid_results and 'Dropout' in valid_results[0]['probabilities']:
             valid_results.sort(key=lambda x: x['probabilities']['Dropout'], reverse=True)
             
        return jsonify(valid_results)
        
    except Exception as e:
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

@app.route('/api/retrain', methods=['POST'])
def retrain_model():
    # Hidden endpoint to trigger retraining if needed
    try:
        from train import main as train_main
        train_main()
        load_model()
        return jsonify({"message": "Model retrained and reloaded"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
