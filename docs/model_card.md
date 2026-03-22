# Model Card — German Credit Risk Baseline

## Model Name
german_credit_logistic_regression

## Business Purpose
Baseline credit risk classification model used to demonstrate an audit-ready Azure ML workflow with governance, documentation, and controlled deployment artefacts.

## Intended Use
Educational and portfolio use only. This model is not intended for live lending decisions or production underwriting.

## Input Features
The model uses borrower-related attributes from the German Credit dataset, including:
- checking status
- duration
- credit history
- purpose
- credit amount
- savings status
- employment
- installment commitment
- personal status / sex
- other parties
- residence since
- property magnitude
- age
- other payment plans
- housing
- existing credits
- job
- number of dependents
- own telephone
- foreign worker

## Output
Binary classification:
- 0 = good credit
- 1 = bad credit

## Model Type
Logistic Regression with preprocessing pipeline:
- median imputation for numeric features
- most-frequent imputation for categorical features
- one-hot encoding for categorical variables

## Performance Metrics
- Accuracy: 0.785
- Precision (bad credit): 0.667
- Recall (bad credit): 0.567
- ROC-AUC: 0.807

## Key Governance Notes
- Traceable training script and saved metrics
- Explicit target mapping documented
- Baseline model intended for controlled experimentation
- Suitable for demonstrating model governance and deployment documentation

## Limitations
- Based on a small historical dataset
- Simplified educational use case
- No fairness assessment included at this stage
- Not suitable for operational credit approval decisions

## Approval Status
Draft / portfolio project
