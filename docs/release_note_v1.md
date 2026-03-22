# Release Note — v1 Baseline Deployment Package

## Release Version
v1

## Scope
Initial baseline deployment package for the German Credit risk classification service on Azure ML.

## Included Artefacts
- baseline trained model (`training/model.pkl`)
- metrics file (`training/metrics.json`)
- artifact metadata (`training/artifact_info.json`)
- scoring script (`deployment/score.py`)
- endpoint config (`deployment/endpoint.yml`)
- deployment config (`deployment/deployment.yml`)
- governance documentation (`docs/model_card.md`, `docs/data_sheet.md`)

## Known Limitations
- Educational portfolio use only
- No fairness evaluation included yet
- No production approval workflow integrated
- No live monitoring or drift detection implemented yet

## Risk Notes
- Historical credit data may contain embedded bias
- Model is not suitable for real lending decisions
- Deployment artefacts are prepared for controlled demonstration only
