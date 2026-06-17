import argparse
import json
import os

DATA_PATH = "data/raw/df_features.csv"


def train(data_path: str, version: str) -> dict:
    print(f"Training {version} with {data_path}")
    # TODO: load data, train model, compute real metrics
    metrics = {"rmse": 0.0, "mae": 0.0, "r2": 0.0, "version": version}
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, choices=["v1", "v2", "v3"])
    args = parser.parse_args()

    metrics = train(DATA_PATH, args.version)

    os.makedirs("metrics", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Done. Metrics: {metrics}")
