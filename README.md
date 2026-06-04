# Customer Churn Prediction API - FastAPI Deployment v1

## Project Overview

This repository represents the second stage of a multi-stage end-to-end Machine Learning project focused on customer churn prediction.

The purpose of this phase is to:
- Serve a trained machine learning model through a REST API
- Create a reproducible inference layer
- Validate real-time prediction workflows
- Prepare the project for cloud deployment

This repository acts as the transition point between traditional machine learning experimentation and production-oriented machine learning engineering.

---

# Project Ecosystem

This repository is part of a complete Machine Learning deployment workflow.

## Repository Flow

| Stage | Repository | Purpose |
|---|---|---|
| 1 | [customer-churn-ml-v1](https://github.com/ImmaniTr/customer-churn-ml-v1) | Data analysis, preprocessing, modeling and evaluation |
| 2 | [customer-churn-ml-api-v1](https://github.com/ImmaniTr/customer-churn-ml-api-v1) | Local FastAPI implementation for real-time predictions |
| 3 | [customer-churn-ml-api-aws-v1](https://github.com/ImmaniTr/customer-churn-ml-api-aws-v1) | Initial AWS deployment using Docker and ECS |
| 4 | [customer-churn-aws-deployment-v1](https://github.com/ImmaniTr/customer-churn-aws-deployment-v1) | Production-oriented deployment with ALB, monitoring and CI/CD |

---

# Project Evolution

This repository introduces the serving layer of the project.

The project later evolved into:
- Docker containerization
- AWS ECS deployment
- Application Load Balancer integration
- CloudWatch monitoring
- CI/CD automation with GitHub Actions

---

## Relationship with the Modeling Repository

The machine learning model used in this repository was developed and packaged in:

[customer-churn-ml-v1](https://github.com/ImmaniTr/customer-churn-ml-v1)

That repository includes:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training and Evaluation
- Final Model Packaging (`churn_pipeline.joblib`)

This repository focuses on exposing the trained model through an API layer for real-time inference.

---

## API Architecture

This repository focuses on the serving layer of the machine learning lifecycle:

- Load trained pipeline
- Expose prediction endpoint through FastAPI
- Handle structured JSON input
- Return predictions and probabilities
- Create reusable inference workflow

---

## API Overview

### Base URL

```bash
http://127.0.0.1:8000
```

### Available Endpoints

#### GET /
Health check endpoint.

#### POST /predict
Returns churn prediction and probability.

#### /docs
Interactive Swagger UI for API testing and schema validation.

---

## Example Request

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

---

## Example Response

```json
{
  "prediction": 1,
  "probability": 0.78
}
```

---

## Setup Instructions

### 1. Create Environment

```bash
conda env create -f environment.yml
conda activate churn-env
```

### 2. Install Dependencies (Optional Fallback)

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Application

```bash
uvicorn main:app --reload
```

### 4. Access Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---

## Model Packaging

The API loads a packaged machine learning pipeline:

```bash
churn_pipeline.joblib
```

The pipeline includes:
- preprocessing
- encoding
- scaling
- feature transformation
- final trained model

Selected model:
- Balanced Random Forest

---

## Workflow Separation

The project intentionally separates responsibilities across repositories.

### Modeling Repository
Repository:
[customer-churn-ml-v1](https://github.com/ImmaniTr/customer-churn-ml-v1)

Focus:
- data analysis
- preprocessing
- feature engineering
- model training
- model evaluation
- packaging

### API Repository (Current Repository)
Repository:
[customer-churn-ml-api-v1](https://github.com/ImmaniTr/customer-churn-ml-api-v1)

Focus:
- FastAPI implementation
- real-time inference
- API serving
- structured input validation
- deployment preparation

---

## Implemented Extensions

The project was later expanded into cloud deployment and MLOps-oriented workflows through additional repositories.

Implemented additions:
- Docker containerization
- AWS ECS deployment
- Application Load Balancer
- CloudWatch monitoring
- CI/CD automation

See:
- [customer-churn-ml-api-aws-v1](https://github.com/ImmaniTr/customer-churn-ml-api-aws-v1)
- [customer-churn-aws-deployment-v1](https://github.com/ImmaniTr/customer-churn-aws-deployment-v1)

---

## Key Insight

This repository demonstrates the transition from:

**Machine Learning Model → Production-Oriented API Service**

It bridges the gap between:
- data science experimentation
- machine learning engineering
- API serving architectures

---

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Uvicorn

---

## Author

**Immani Trejo**  
Data Science | Machine Learning | Cloud Deployment

Background in:
- IT consulting
- machine learning
- data analysis
- cloud deployment
- end-to-end ML workflows

---

## Recruiter Note

This repository demonstrates the transition from a trained machine learning model to a production-oriented inference service.

It showcases the ability to:
- package machine learning pipelines
- expose real-time prediction endpoints
- design reproducible inference workflows
- build API-based ML services using FastAPI

This repository represents the serving layer of a broader end-to-end Machine Learning ecosystem that later evolved into:
- AWS deployment
- monitoring
- CI/CD automation
- production-oriented infrastructure
