# Azure Credit Risk ML

End-to-end Machine Learning project for credit risk prediction using Azure Machine Learning.

## Objective
Build a production-ready ML workflow for a regulated finance use case:
- train a credit risk classifier
- track experiments
- register the model in Azure ML
- deploy a managed online endpoint
- expose a prediction API

## Tech Stack
- Python
- scikit-learn
- Azure Machine Learning
- FastAPI
- MLflow
- Docker

## Project Structure
azure-credit-risk-ml/
│
├── data/                # datasets
├── training/            # model training scripts
├── src/                 # utilities / connection scripts
├── deployment/          # endpoint deployment configs
├── notebooks/           # experimentation notebooks
├── requirements.txt
└── README.md

## Dataset
German Credit dataset (UCI repository) used to train a credit risk classification model.

## Workflow
1. Data ingestion
2. Feature preprocessing
3. Model training and evaluation
4. Experiment tracking
5. Model registry in Azure ML
6. Deployment of prediction service

## Goal
Demonstrate an end-to-end ML engineering pipeline suitable for regulated financial environments.
