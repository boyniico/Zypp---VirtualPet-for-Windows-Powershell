import json

def load_json(filename: str):
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(filename: str, data: dict):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)