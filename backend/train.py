import os
from model import DropoutPredictor

def main():
    # Path to data
    # Assuming this script is run from the project root or backend/
    # Try finding the file in likely locations
    possible_paths = [
        "research-space/final-project-data.csv",
        "../research-space/final-project-data.csv",
        "/Users/bhislop/Documents/school/classes/2025-8-fall/cs-3210-machine/cs3120-final-project/research-space/final-project-data.csv"
    ]
    
    data_path = None
    for path in possible_paths:
        if os.path.exists(path):
            data_path = path
            break
            
    if data_path is None:
        print("Error: Could not find final-project-data.csv")
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
