from schemapie.utils.os import display, read, write
import requests

def flatten(data: dict | list, path: str = "", meta: dict = {}):
    """Flattens each object in the API response into a dictionary object containing {path: details}."""
    if isinstance(data, dict):
        for k, v in data.items():
            meta[f"{path}{k}"] = {"path": path if path else None, "type": type(v).__name__}
            if isinstance(v, (dict, list)):
                flatten(data=v, path=f"{path}{k}.", meta=meta)
            else:
                meta[f"{path}{k}"].update({"example": v})

    elif isinstance(data, list):
        for v in data:
            flatten(data=v, path=path, meta=meta)

    return meta

def merge(meta: dict, schema: dict = {}):
    """Loops through the flattened API response data that was created by the flatten function."""
    for key, value in meta.items():
        path = key.split('.')
        build(schema=schema, path=path, value=value)

    return schema

def build(schema: dict, path: list, value: dict):
    """Constructs the schema one object at a time."""
    current = schema
    for i, p in enumerate(path):
        if p not in current:
            current[p] = {}

        if i == len(path) - 1:
            current[p].update(value)
        else:
            current[p].setdefault("children", {})
            current = current[p]["children"]

def execute(url: str, file: str = None):
    print(f"Fetching data from {url}...")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meta = flatten(data)
        schema = merge(meta=meta, schema=read(file=file) if file else {})
        write(schema=schema, file=file) if file else display(schema=schema)
    else:
        print(f"Error: {response.status_code} - {response.text}")