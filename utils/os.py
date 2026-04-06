import json
import os

def read(endpoint: str, directory: str):
    filename = f'{endpoint.replace("/", ".")}.json'
    filepath = os.path.join(directory, filename)

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            print(f"Sourcing schema from {filepath}...")
            return json.load(file)
    else:
        print(f"Failed to find schema from {filepath}. Proceeding with empty schema...")
        return {}

def write(schema: dict, endpoint: str, directory: str):
    filename = f'{endpoint.replace("/", ".")}.json'
    filepath = os.path.join(directory, filename)

    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(filepath, 'w') as file:
        json.dump(schema, file, indent=2)
        print(f"Schema saved to {filepath}!")