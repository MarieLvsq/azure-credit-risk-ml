# Azure Credit Risk ML — Audit-Ready ML System

End-to-end Machine Learning project demonstrating a **governed, auditable, and traceable credit risk system** built using Azure Machine Learning.

---

## Objective

Build a credit risk classification system aligned with **IT Risk and Governance, Risk & Compliance (GRC)** principles:

- controlled model training
- traceable predictions
- documented artefacts
- audit-ready deployment package
- monitoring and risk management

---

## Why This Project Matters

Traditional ML projects focus only on accuracy.

This project focuses on:

- auditability
- traceability
- governance
- controlled deployment

These are critical in:

- banking
- insurance
- fintech
- regulated AI systems

---

## System Overview

~~~text
Data -> Training -> Model Artefacts -> Deployment -> Monitoring -> Governance
~~~

## Key Components

### 1. Data Layer
- UCI German Credit dataset
- structured and documented (data sheet)

### 2. Training Layer
- preprocessing pipeline
- logistic regression model
- metrics recorded and saved

### 3. Artefacts
- model.pkl
- metrics.json
- artifact_info.json

### 4. Deployment Layer
- scoring API (`score.py`)
- Azure ML endpoint configuration

### 5. Governance Layer
- model card
- data sheet
- risk register
- monitoring plan
- deployment checklist
- rollback plan
- release notes

---

## Traceability Features

Each prediction includes:

- request_id
- timestamp
- model version
- input features
- prediction output

This enables:

- audit trails
- reproducibility
- investigation of decisions

---

## Monitoring & Risk Management

- performance tracking (accuracy, recall, ROC-AUC)
- data drift awareness
- error tracking
- risk register documentation

---

## Governance Artefacts

Located in `/docs`:

- model_card.md
- data_sheet.md
- risk_register.md
- monitoring_plan.md
- deployment_checklist.md
- rollback_plan.md
- release_note_v1.md

---

## Azure Role

Azure Machine Learning enables:

- model lifecycle management
- controlled deployment
- versioning
- scalable endpoints

This supports **enterprise-grade ML governance**.

---

## Relevance to IT Risk & GRC

This project demonstrates:

- model governance
- auditability
- traceable decision systems
- risk identification and mitigation
- controlled deployment practices

Aligned with:

- Basel III
- GDPR
- operational resilience frameworks
- AI governance requirements

---

## Limitations

- educational dataset
- no fairness analysis yet
- no real production deployment
- simplified model

---

## Future Improvements

- fairness and bias evaluation
- explainability (SHAP / LIME)
- real Azure endpoint deployment
- CI/CD integration
- automated monitoring
