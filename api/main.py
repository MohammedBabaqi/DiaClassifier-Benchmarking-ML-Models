from fastapi import FastAPI, HTTPException
from api.schemas import DiabetesInput, PredictionResponse, ModelMetadata
from api.model_utils import load_model, predict, get_bundle_metadata
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Diabetes Classification API",
    description="Professional API for predicting diabetes risk using XGBoost",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """
    Load the model bundle on application startup.
    """
    try:
        load_model()
        logger.info("Application started and model loaded.")
    except Exception as e:
        logger.error(f"Failed to load model on startup: {e}")
        # In a production environment, you might want to exit here
        # or handle this via a healthy check status

@app.get("/", tags=["General"])
async def root():
    return {"message": "Welcome to the Diabetes Classification API. Visit /docs for documentation."}

@app.get("/health", tags=["General"])
async def health_check():
    """
    Endpoint for health monitoring.
    """
    try:
        load_model()
        return {"status": "healthy", "model_loaded": True}
    except Exception:
        return {"status": "unhealthy", "model_loaded": False}

@app.get("/metadata", response_model=ModelMetadata, tags=["Model"])
async def get_metadata():
    """
    Returns information about the model, including version and required features.
    """
    try:
        return get_bundle_metadata()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict", response_model=PredictionResponse, tags=["Model"])
async def make_prediction(input_data: DiabetesInput):
    """
    Endpoint to perform diabetes risk prediction.
    """
    try:
        # Convert Pydantic model to dict
        data = input_data.dict()
        # Perform prediction
        result = predict(data)
        return result
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
