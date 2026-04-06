import json
import os

def display(schema: dict):
    print(json.dumps(schema, indent=2))

def read(file: str):
    filepath = os.path.abspath(file)

    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            print(f"Sourcing schema from {filepath}...")
            return json.load(file)
    else:
        print(f"No source schema found from {filepath}.")
        print("Proceeding with an empty schema...")
        return {}

def write(schema: dict, file: str):
    filepath = os.path.abspath(file)
    directory = os.path.dirname(filepath)

    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(filepath, 'w') as file:
        json.dump(schema, file, indent=2)
        print(f"Schema saved to {filepath}!")