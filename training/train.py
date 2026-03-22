import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# ----------------------------
# Config
# ----------------------------
DATA_PATH = Path("data/german.data")
MODEL_PATH = Path("training/model.pkl")
METRICS_PATH = Path("training/metrics.json")
ARTIFACT_INFO_PATH = Path("training/artifact_info.json")

COLUMN_NAMES = [
    "checking_status",
    "duration",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_status",
    "employment",
    "installment_commitment",
    "personal_status_sex",
    "other_parties",
    "residence_since",
    "property_magnitude",
    "age",
    "other_payment_plans",
    "housing",
    "existing_credits",
    "job",
    "num_dependents",
    "own_telephone",
    "foreign_worker",
    "target",
]

RANDOM_STATE = 42
TEST_SIZE = 0.2

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv(DATA_PATH, sep=" ", header=None, names=COLUMN_NAMES)

# Map target to binary:
# UCI original convention commonly uses:
# 1 = good credit
# 2 = bad credit
# For this project:
# 0 = good credit
# 1 = bad credit
df["target"] = df["target"].map({1: 0, 2: 1})

if df["target"].isna().any():
    raise ValueError("Target mapping failed; unexpected target values found.")

X = df.drop(columns=["target"])
y = df["target"]

categorical_features = X.select_dtypes(include=["object"]).columns.tolist()
numeric_features = X.select_dtypes(exclude=["object"]).columns.tolist()

# ----------------------------
# Preprocessing
# ----------------------------
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

# ----------------------------
# Model pipeline
# ----------------------------
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)),
    ]
)

# ----------------------------
# Split data
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y,
)

# ----------------------------
# Train
# ----------------------------
model.fit(X_train, y_train)

# ----------------------------
# Evaluate
# ----------------------------
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

metrics = {
    "model_name": "german_credit_logistic_regression",
    "business_use_case": "baseline risk classification for governance-oriented Azure ML demo",
    "training_timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "dataset_rows": int(df.shape[0]),
    "dataset_columns": int(df.shape[1]),
    "train_rows": int(X_train.shape[0]),
    "test_rows": int(X_test.shape[0]),
    "target_definition": {
        "0": "good_credit",
        "1": "bad_credit",
    },
    "test_size": TEST_SIZE,
    "random_state": RANDOM_STATE,
    "accuracy": float(accuracy_score(y_test, y_pred)),
    "precision_bad_credit": float(precision_score(y_test, y_pred, zero_division=0)),
    "recall_bad_credit": float(recall_score(y_test, y_pred, zero_division=0)),
    "roc_auc": float(roc_auc_score(y_test, y_proba)),
    "numeric_features": numeric_features,
    "categorical_features": categorical_features,
}

artifact_info = {
    "model_path": str(MODEL_PATH),
    "metrics_path": str(METRICS_PATH),
    "artifact_created_utc": datetime.now(timezone.utc).isoformat(),
    "deployment_note": "Baseline artifact for controlled deployment and governance documentation.",
}

# ----------------------------
# Save outputs
# ----------------------------
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(model, MODEL_PATH)

with open(METRICS_PATH, "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

with open(ARTIFACT_INFO_PATH, "w", encoding="utf-8") as f:
    json.dump(artifact_info, f, indent=2)

# ----------------------------
# Print summary
# ----------------------------
print("Training completed.")
print(f"Model saved to: {MODEL_PATH}")
print(f"Metrics saved to: {METRICS_PATH}")
print(f"Artifact info saved to: {ARTIFACT_INFO_PATH}")
print()
print("Classification report:")
print(classification_report(y_test, y_pred, target_names=["good_credit", "bad_credit"], zero_division=0))
print("Metrics summary:")
for key in ["accuracy", "precision_bad_credit", "recall_bad_credit", "roc_auc"]:
    print(f"{key}: {metrics[key]:.4f}")
