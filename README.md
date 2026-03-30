# Customer Churn Prediction - AWS Deployment (v1)

##  Overview
This repository contains the deployment phase of a Customer Churn Prediction project. The objective is to expose a trained machine learning model through an API and prepare it for cloud deployment.

The model used in this project was developed and packaged in a previous repository:

https://github.com/ImmaniTr/customer-churn-ml-v1

That repository includes:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training and Evaluation
- Final Model Packaging (`churn_pipeline.joblib`)

---

## Project Architecture

This project focuses on the serving layer of the machine learning lifecycle:

- Load trained model (pipeline)
- Expose prediction endpoint via FastAPI
- Handle structured JSON input
- Return predictions and probabilities

---

##  API Overview

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### GET /
Health check endpoint

#### POST /predict
Returns churn prediction and probability.

#### INTERFACE FOR INTERACTING /docs
Customer Churn Prediction API.

### Example Request
```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 85.5,
  "TotalCharges": 1026.0
}
```

### Example Response
```json
{
  "prediction": 1,
  "probability": 0.78
}
```

---

##  Setup Instructions

### 1. Create environment
```
conda env create -f environment.yml
conda activate churn-env
```

### 2. Install dependencies (optional fallback)
```
pip install -r requirements.txt
```

### 3. Run API
```
uvicorn main:app --reload
```

### 4. Access Swagger UI
```
http://127.0.0.1:8000/docs
```

---

##  Model

The model used in this API is a packaged pipeline:

```
churn_pipeline.joblib
```

It includes:
- Preprocessing (encoding, scaling)
- Feature transformation
- Final trained model (Random Forest - balanced)

---

##  Workflow Separation

This project follows a two-repository structure:

### Repo 1 → Modeling
customer-churn-ml-v1  
Focus: Data analysis, modeling, evaluation, and packaging

### Repo 2 → Deployment (this repo)
Focus: API, serving, and cloud readiness

---

##  Next Steps

- Containerization with Docker
- Deployment on AWS (EC2 / ECS)
- CI/CD with GitHub Actions
- Monitoring and logging

---

##  Key Insight

This project demonstrates the transition from:
**Machine Learning Model → Production-Ready Service**

---

##  Author
**Immani Trejo**  
Data Science | Machine Learning | IT Background  

Experience in data analysis, applied statistics, machine learning, and cloud-based deployment.


## 📌 Recruiter Note

This project demonstrates the end-to-end transition from a machine learning model to a production-ready API.

It showcases the ability to:
- Package a trained ML pipeline (including preprocessing and model)
- Serve real-time predictions using FastAPI
- Design a clean and reproducible deployment structure
- Bridge the gap between data science and machine learning engineering

This repository focuses on the deployment layer.  
The full modeling process (EDA, feature engineering, and model selection) is available in a separate repository.

https://github.com/ImmaniTr/customer-churn-ml-v1
