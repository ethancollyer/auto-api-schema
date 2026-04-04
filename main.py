import requests
import argparse
import json

def recurse(data: dict | list, depth: int = 0):
    meta = {}
    if isinstance(data, dict):
        for k, v in data.items(): 
            meta[k] = {"depth": depth, "type": type(v).__name__, "children": recurse(data=data.get(k), depth=depth + 1) if isinstance(v, (dict, list)) else False }
    if isinstance(data, list):
        for k, v in enumerate(data):
            meta["Object"] = {"depth": depth, "type": type(v).__name__, "children": recurse(data=data[k], depth=depth + 1) if isinstance(v, (dict, list)) else False }
    
    return meta

def main(domain: str, endpoint: str, params: dict):
    url = f"https://{domain}/{endpoint.format(**params)}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meta = recurse(data)
        
        with open(f'{endpoint.replace('/', '.')}.json', 'w') as file:
            file.writelines(json.dumps(obj=meta, indent=2, default=str))
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", type=str, required=True)
    parser.add_argument("--params", type=str, default="{}")
    args = parser.parse_args()

    main(domain="domain.com", endpoint=args.endpoint, params=json.loads(args.params))