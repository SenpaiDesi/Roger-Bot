import json


def get_json(path):
    with open(path, "r") as f:
        return json.load(f)