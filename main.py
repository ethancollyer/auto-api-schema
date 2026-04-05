import requests
import argparse
import json

def digest(data: dict | list, depth: int = 0, path: str = "", meta: dict = {}):
    """Flattens each object in the API response into a dictionary object containing {path: details}."""
    if isinstance(data, dict):
        for k, v in data.items():
            meta[f"{path}{k}"] = {"depth": depth, "type": type(v).__name__}
            if isinstance(v, (dict, list)):
                digest(data=v, depth=depth + 1, path=f"{path}{k}/", meta=meta)
            else:
                meta[f"{path}{k}"].update({"example": v})

    elif isinstance(data, list):
        for v in data:
            digest(data=v, depth=depth, path=path, meta=meta)

    return meta

def build(meta: dict):
    """Loops through the flattened API response data that was created by the digest function."""
    schema = {}
    for key, value in meta.items():
        path = key.split('/')
        merge(schema=schema, path=path, value=value)

    return schema

def merge(schema: dict, path: list, value: dict):
    """Constructs the nested schema tree, one object at a time."""
    current = schema
    for i, p in enumerate(path):
        if p not in current:
            current[p] = {}

        if i == len(path) - 1:
            current[p].update(value)
        else:
            current[p].setdefault("children", {})
            current = current[p]["children"]

def main(domain: str, endpoint: str, params: dict):
    url = f"https://{domain}/{endpoint.format(**params)}"
    print(f"Fetching data from {url}...")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meta = digest(data)
        schema = build(meta)

        with open(f'{endpoint.replace("/", ".")}.json', 'w') as file:
            json.dump(schema, file, indent=2)
            print(f"Schema saved to {file.name}")

    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", type=str, required=True)
    parser.add_argument("--endpoint", type=str, required=True)
    parser.add_argument("--params", type=str, default="{}")
    args = parser.parse_args()

    main(domain=args.domain, endpoint=args.endpoint, params=json.loads(args.params))