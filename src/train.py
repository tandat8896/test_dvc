import argparse
import csv
import json
import os

import dvc.api


def train(version: str) -> dict:
    with dvc.api.open("data/raw/df_features.csv", rev=version, mode="r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    n_rows = len(rows)
    n_features = len(rows[0]) - 2 if rows else 0  # tru cot id va label

    print(f"[{version}] {n_rows} rows, {n_features} features")

    # TODO: thay bang model thuc su
    metrics = {
        "version": version,
        "n_rows": n_rows,
        "n_features": n_features,
        "rmse": round(1.0 / (n_rows * 0.1), 4),
        "mae": round(0.8 / (n_rows * 0.1), 4),
        "r2": round(1 - 1 / n_rows, 4),
    }
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    metrics = train(args.version)

    os.makedirs("metrics", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Metrics: {metrics}")
