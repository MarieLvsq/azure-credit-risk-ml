import json
import os
from datetime import datetime, timezone
import uuid

import joblib
import pandas as pd

model = None

MODEL_NAME = "german_credit_logistic_regression"
MODEL_VERSION = "v1"
MODEL_STAGE = "baseline"

def init():
    global model
    model_path = os.path.join(os.path.dirname(__file__), "..", "training", "model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        payload = json.loads(raw_data)

        if isinstance(payload, dict):
            data = [payload]
        elif isinstance(payload, list):
            data = payload
        else:
            raise ValueError("Invalid input format")

        df = pd.DataFrame(data)

        probabilities = model.predict_proba(df)[:, 1]
        predictions = model.predict(df)

        results = []
        timestamp = datetime.now(timezone.utc).isoformat()

        for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
            results.append({
                "request_id": str(uuid.uuid4()),
                "row_index": i,
                "timestamp_utc": timestamp,
                "model_name": MODEL_NAME,
                "model_version": MODEL_VERSION,
                "model_stage": MODEL_STAGE,
                "prediction_code": int(pred),
                "prediction_label": "bad_credit" if int(pred) == 1 else "good_credit",
                "probability_bad_credit": float(prob),
                "features": data[i]  # traceability
            })

        return {"results": results}

    except Exception as e:
        return {
            "error": str(e),
            "model_name": MODEL_NAME
        }
