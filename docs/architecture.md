# Architecture Overview — Credit Risk ML System

## Components

1. Data Layer
- UCI German Credit dataset

2. Training Layer
- Python (scikit-learn)
- preprocessing pipeline
- logistic regression model

3. Artefacts
- model.pkl
- metrics.json
- artifact_info.json

4. Deployment Layer
- Azure ML (managed endpoint)
- scoring script

5. Governance Layer
- model card
- data sheet
- risk register
- monitoring plan
- deployment checklist
- release notes

## Key Design Principle
Separation between:
- model logic
- deployment
- governance artefacts

## Objective
Enable:
- traceability
- auditability
- controlled deployment
