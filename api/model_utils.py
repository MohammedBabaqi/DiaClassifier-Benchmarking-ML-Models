import joblib
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

# Cache for the model bundle
_model_bundle = None

def load_model(model_path: str = "model/diabetes_bundle.pkl"):
    """
    Loads the model bundle from the specified path.
    """
    global _model_bundle
    if _model_bundle is None:
        if not os.path.exists(model_path):
            # Try relative to the script's directory if absolute fails or is not found
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            model_path = os.path.join(base_dir, "model", "diabetes_bundle.pkl")
            
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model bundle not found at {model_path}")
            
        logger.info(f"Loading model bundle from {model_path}...")
        _model_bundle = joblib.load(model_path)
        logger.info("Model bundle loaded successfully.")
    return _model_bundle

def predict(data_dict: dict):
    """
    Performs prediction using the loaded model and custom threshold.
    """
    bundle = load_model()
    model = bundle["model"]
    threshold = bundle["threshold"]
    features = bundle["features"]

    # Convert dictionary to DataFrame with correct feature order
    df = pd.DataFrame([data_dict])[features]

    # Get probability for the positive class (Diabetes)
    # Calibrated classifiers or pipelines usually have predict_proba
    probs = model.predict_proba(df)[:, 1]
    prob = float(probs[0])

    # Assign class based on custom threshold
    prediction = 1 if prob >= threshold else 0

    return {
        "prediction": prediction,
        "probability": prob,
        "threshold_used": threshold,
        "model_name": bundle["model_name"],
        "version": bundle["version"]
    }

def get_bundle_metadata():
    """
    Returns metadata about the loaded model.
    """
    bundle = load_model()
    return {
        "model_name": bundle["model_name"],
        "version": bundle["version"],
        "threshold": bundle["threshold"],
        "features": bundle["features"]
    }
