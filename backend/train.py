import os
from model import DropoutPredictor

def main():
    # Path to data
    # Assuming this script is run from the project root
    data_path = "research-space/final-project-data.csv"
    
    if not os.path.exists(data_path):
        print(f"Error: Could not find {data_path}")
        print("Please run this script from the project root directory.")
        return

    model_path = "backend/model_artifacts.joblib" if os.path.exists("backend") else "model_artifacts.joblib"
    
    print(f"Training model using data from: {data_path}")
    
    predictor = DropoutPredictor()
    try:
        metrics = predictor.train(data_path)
        print(f"Training complete. Training accuracy: {metrics['accuracy']:.4f}")
        
        predictor.save(model_path)
        print(f"Model saved to {model_path}")
    except Exception as e:
        print(f"Error during training: {e}")

if __name__ == "__main__":
    main()
