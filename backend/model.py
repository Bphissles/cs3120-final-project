import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import joblib
import os

class DropoutPredictor:
    def __init__(self):
        self.model = None
        self.encoder = None
        self.categorical_columns = None
        self.feature_columns = None
        self.target_mapping = None # To map prediction back to label if needed

    def clean_data(self, df):
        # Cleaning steps from notebook
        df.columns = [
            column.replace("\ufeff", "").strip().strip('"') for column in df.columns
        ]
        return df

    def train(self, data_path):
        # Load data
        df = pd.read_csv(data_path, sep=";", na_values=["", " "])
        df = self.clean_data(df)
        
        # Define Top 10 features
        top_features = [
            "Curricular units 2nd sem (approved)",
            "Curricular units 2nd sem (grade)",
            "Curricular units 1st sem (approved)",
            "Curricular units 1st sem (grade)",
            "Tuition fees up to date",
            "Curricular units 2nd sem (evaluations)",
            "Curricular units 1st sem (evaluations)",
            "Age at enrollment",
            "Course",
            "Curricular units 2nd sem (enrolled)"
        ]
        
        # Filter dataframe to keep only top features + Target
        if "Target" in df.columns:
            df = df[top_features + ["Target"]]
        
        # Identify target and features
        target_column = "Target"
        if target_column not in df.columns:
             raise ValueError("Target column not found in data")
             
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Store feature columns
        self.feature_columns = X.columns.tolist()
        
        # Identify categorical columns in the subset
        self.categorical_columns = X.select_dtypes(include=["object", "category"]).columns.tolist()
        
        # Encoding
        # We'll just use factorize for simplicity like the notebook or OrdinalEncoder
        # Ideally we save the encoder. Let's use OrdinalEncoder for consistency
        if self.categorical_columns:
            self.encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
            X[self.categorical_columns] = self.encoder.fit_transform(X[self.categorical_columns])
            
        # Model Parameters (Best from Notebook)
        # {'max_depth': 10, 'min_samples_leaf': 10, 'class_weight': 'balanced_subsample'}
        self.model = RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            max_depth=10,
            min_samples_leaf=10,
            class_weight="balanced_subsample"
        )
        
        self.model.fit(X, y)
        print("Model trained successfully on Top 10 features.")
        # Calculate basic metrics
        accuracy = self.model.score(X, y)
        return {"accuracy": accuracy}

    def predict(self, data):
        """
        data: pd.DataFrame or list of dicts
        """
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = data.copy()
            
        # Ensure columns match (handling missing or extra columns if necessary, though strict is better)
        # For now assume input matches schema
        
        # Clean columns just in case
        df = self.clean_data(df)
        
        # Check for missing columns and add them as 0/NaN if needed, or raise error
        # Ideally the input form matches the schema exactly.
        
        # Transform categorical
        if self.categorical_columns:
            # Ensure all categorical columns exist
            for col in self.categorical_columns:
                if col not in df.columns:
                    df[col] = "" # or some default
            
            df[self.categorical_columns] = self.encoder.transform(df[self.categorical_columns])
            
        # Reorder columns to match training
        df = df[self.feature_columns]
        
        predictions = self.model.predict(df)
        probabilities = self.model.predict_proba(df)
        
        # Get class order
        classes = self.model.classes_
        
        results = []
        for pred, prob in zip(predictions, probabilities):
            # Find max probability
            confidence = max(prob)
            results.append({
                "prediction": pred,
                "confidence": float(confidence),
                "probabilities": {cls: float(p) for cls, p in zip(classes, prob)}
            })
            
        return results

    def save(self, path):
        joblib.dump({
            "model": self.model,
            "encoder": self.encoder,
            "categorical_columns": self.categorical_columns,
            "feature_columns": self.feature_columns
        }, path)

    def load(self, path):
        artifacts = joblib.load(path)
        self.model = artifacts["model"]
        self.encoder = artifacts["encoder"]
        self.categorical_columns = artifacts["categorical_columns"]
        self.feature_columns = artifacts["feature_columns"]
