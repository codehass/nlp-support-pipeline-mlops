import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

MODEL_PATH = "notebooks/best_email_classifier.pkl"
TRANSFORMER_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"


def load_pipeline():
    print("--- Loading AI Pipeline ---")

    artifacts = joblib.load(MODEL_PATH)
    embedder = SentenceTransformer(TRANSFORMER_MODEL)

    print("Pipeline loaded successfully.")
    return artifacts, embedder


def predict_single_ticket(text, metadata, artifacts, embedder):
    text_features = embedder.encode([text])

    meta_df = pd.DataFrame([metadata])

    expected_columns = artifacts["categorical_encoder"].feature_names_in_

    meta_df_filtered = meta_df[expected_columns]

    meta_features = (
        artifacts["categorical_encoder"].transform(meta_df_filtered).toarray()
    )

    X_combined = np.hstack((text_features, meta_features))

    pred_num = artifacts["classifier"].predict(X_combined.astype(np.float32))
    label = artifacts["label_encoder"].inverse_transform(pred_num)

    return label[0]


if __name__ == "__main__":
    artifacts, embedder = load_pipeline()

    test_email = "My password is not working and I cannot log into the VPN"
    test_meta = {
        "priority": "High",
        "queue": "IT Support",
        "language": "en",
        "tag_1": "Access",
        "tag_2": "Authentication",
        "tag_3": "Internal",
    }

    result = predict_single_ticket(test_email, test_meta, artifacts, embedder)

    print("\n--- Test Result ---")
    print(f"Text: {test_email}")
    print(f"Predicted Category: **{result}**")
