# -----------------------------
# Imports
# -----------------------------

# FastAPI is used to create the API
from fastapi import FastAPI

# Pydantic is used for data validation and schema definition
from pydantic import BaseModel

# Pandas is used to convert input data into a DataFrame
import pandas as pd

# Joblib is used to load the trained machine learning model
import joblib


# -----------------------------
# Initialize FastAPI application
# -----------------------------

app = FastAPI(
    title="Customer Churn Prediction API",
    description="API that predicts customer churn probability using a trained ML model",
    version="1.0"
)


# -----------------------------
# Load trained model
# -----------------------------

# This file contains the full pipeline:
# - data preprocessing (scaling, encoding, etc.)
# - trained machine learning model
model = joblib.load("churn_pipeline.joblib")


# -----------------------------
# Define input data schema
# -----------------------------

# This class validates incoming requests automatically:
# - ensures correct data types
# - ensures required fields are present
# - helps generate API documentation (Swagger)
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


# -----------------------------
# Health check endpoint
# -----------------------------

# This endpoint is used to verify that the API is running correctly
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


# -----------------------------
# Main prediction endpoint
# -----------------------------

@app.post("/predict")
def predict(customer: CustomerData):

    # Convert incoming JSON data into a DataFrame
    # The model expects the same structure used during training
    data = pd.DataFrame([customer.model_dump()])

    # Generate prediction (0 = no churn, 1 = churn)
    prediction = model.predict(data)[0]

    # Generate probability of churn (value between 0 and 1)
    probability = model.predict_proba(data)[0][1]

    # Return results as JSON response
    return {
        "prediction": int(prediction),
        "churn_probability": float(probability)
    }