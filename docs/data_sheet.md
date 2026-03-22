# Data Sheet — German Credit Dataset

## Dataset Name
Statlog German Credit Data

## Source
Official UCI Statlog German Credit dataset stored locally in:
- `data/german.data`
- `data/german.doc`

## Use Case
Binary classification for borrower credit risk.

## Record Count
1000 rows

## Schema
20 input features plus 1 target field.

## Target Variable
Original dataset target values:
- 1 = good credit
- 2 = bad credit

Project mapping:
- 0 = good credit
- 1 = bad credit

## Data Format
Raw source file is space-separated with coded categorical values.

## Data Preparation
- Column names assigned explicitly in the training script
- Categorical values retained as coded categories
- Missing values handled through imputation pipeline
- Categorical variables encoded with one-hot encoding

## Data Quality Notes
- Legacy coded feature values require documentation
- Raw values are compact and not business-friendly without mapping tables
- Suitable for controlled ML experimentation, not direct production use

## Bias / Risk Considerations
- Historical credit datasets may reflect embedded demographic or socioeconomic bias
- Further fairness and subgroup analysis would be required before any production-like use
- This project uses the dataset strictly for educational and portfolio demonstration

## Regulatory / Governance Relevance
This dataset supports a demonstration of:
- model documentation
- traceable preprocessing
- metrics capture
- controlled deployment preparation
- audit-oriented ML lifecycle practices
