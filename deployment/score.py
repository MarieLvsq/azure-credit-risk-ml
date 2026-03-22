import json
import os
from datetime import datetime, timezone

import joblib
import pandas as pd

model = None

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
            raise ValueError("Input payload must be a JSON object or a list of JSON objects.")

        df = pd.DataFrame(data)

        probabilities = model.predict_proba(df)[:, 1]
        predictions = model.predict(df)

        results = []
        request_ts = datetime.now(timezone.utc).isoformat()

        for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
            results.append({
                "request_id": f"req-{i:03d}",
                "timestamp_utc": request_ts,
                "prediction_code": int(pred),
                "prediction_label": "bad_credit" if int(pred) == 1 else "good_credit",
                "probability_bad_credit": float(prob),
                "model_name": "german_credit_logistic_regression",
                "model_stage": "baseline"
            })

        return {"results": results}

    except Exception as e:
        return {
            "error": str(e),
            "model_name": "german_credit_logistic_regression"
        }
