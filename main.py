from utils.api import digest, build
from utils.os import read, write
import requests
import argparse
import json
import os

def main(domain: str, endpoint: str, params: dict, dir: str):
    url = f"https://{domain}/{endpoint.format(**params)}"
    print(f"Fetching data from {url}...")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meta = digest(data)
        schema = build(meta=meta, schema=read(endpoint=endpoint, directory=dir))

        write(schema=schema, endpoint=endpoint, directory=dir)

    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", type=str, required=True)
    parser.add_argument("--endpoint", type=str, required=True)
    parser.add_argument("--params", type=str, default="{}")
    parser.add_argument("--dir", type=str, default=os.getcwd())
    args = parser.parse_args()

    main(domain=args.domain, endpoint=args.endpoint, params=json.loads(args.params), dir=args.dir)