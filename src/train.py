import argparse
import json
import os

import dvc.api
import yaml


def load_params():
    with open("params.yaml") as f:
        return yaml.safe_load(f)


def load_data(version: str, data_versions: dict) -> bytes:
    rev = data_versions[version]
    with dvc.api.open("data/raw/df_features.csv", rev=rev, mode="rb") as f:
        return f.read()


def train(version: str, data_versions: dict) -> dict:
    data = load_data(version, data_versions)
    print(f"Training {version} | data size: {len(data)} bytes")
    # TODO: parse data, train model, tinh metrics thuc su
    metrics = {"rmse": 0.0, "mae": 0.0, "r2": 0.0, "version": version}
    return metrics


if __name__ == "__main__":
    params = load_params()
    data_versions = params["data_versions"]

    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, choices=list(data_versions.keys()))
    args = parser.parse_args()

    metrics = train(args.version, data_versions)

    os.makedirs("metrics", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    with open("metrics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Done. Metrics: {metrics}")
