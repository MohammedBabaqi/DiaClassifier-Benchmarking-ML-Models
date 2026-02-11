from pydantic import BaseModel, Field
from typing import List, Optional

class DiabetesInput(BaseModel):
    HighBP: float = Field(..., description="High Blood Pressure (0 or 1)")
    HighChol: float = Field(..., description="High Cholesterol (0 or 1)")
    DiffWalk: float = Field(..., description="Difficulty Walking (0 or 1)")
    HeartDiseaseorAttack: float = Field(..., description="Heart Disease or Attack (0 or 1)")
    PhysActivity: float = Field(..., description="Physical Activity (0 or 1)")
    HvyAlcoholConsump: float = Field(..., description="Heavy Alcohol Consumption (0 or 1)")
    CholCheck: float = Field(..., description="Cholesterol Check (0 or 1)")
    Smoker: float = Field(..., description="Smoker (0 or 1)")
    Stroke: float = Field(..., description="Stroke (0 or 1)")
    Sex: float = Field(..., description="Sex (0 for Female, 1 for Male)")
    BMI: float = Field(..., description="Body Mass Index")
    Age: float = Field(..., description="Age category")
    Income: float = Field(..., description="Income category")
    GenHlth: float = Field(..., description="General Health score")
    MentHlth: float = Field(..., description="Mental Health score")
    PhysHlth: float = Field(..., description="Physical Health score")
    Education: float = Field(..., description="Education category")

    class Config:
        json_schema_extra = {
            "example": {
                "HighBP": 0.0,
                "HighChol": 0.0,
                "DiffWalk": 0.0,
                "HeartDiseaseorAttack": 0.0,
                "PhysActivity": 1.0,
                "HvyAlcoholConsump": 0.0,
                "CholCheck": 1.0,
                "Smoker": 0.0,
                "Stroke": 0.0,
                "Sex": 0.0,
                "BMI": 25.0,
                "Age": 5.0,
                "Income": 7.0,
                "GenHlth": 2.0,
                "MentHlth": 0.0,
                "PhysHlth": 0.0,
                "Education": 6.0
            }
        }

class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="Predicted class (0 for No Diabetes, 1 for Diabetes)")
    probability: float = Field(..., description="Probability of Diabetes")
    threshold_used: float = Field(..., description="The decision threshold used for classification")
    model_name: str
    version: str

class ModelMetadata(BaseModel):
    model_name: str
    version: str
    threshold: float
    features: List[str]
