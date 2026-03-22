# Monitoring Plan — Credit Risk Model

## Objective
Ensure traceability, reliability, and risk control of model predictions.

## Key Monitoring Dimensions

### 1. Prediction Logging
Each prediction includes:
- request_id
- timestamp
- model version
- input features
- output prediction

### 2. Data Drift Monitoring
Monitor changes in:
- credit_amount
- duration
- age
- categorical distributions

### 3. Performance Monitoring
Track:
- accuracy over time
- false negatives (bad credit predicted as good)
- ROC-AUC degradation

### 4. Error Monitoring
Track:
- failed inference requests
- schema mismatches
- API errors

## Alerting Triggers
- sudden drop in recall for bad_credit
- abnormal input distribution
- repeated inference errors

## Governance Note
Monitoring is required for:
- model risk management
- operational risk control
- auditability under regulated environments
