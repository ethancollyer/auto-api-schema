from utils.os import display, read, write
from utils.api import digest, build
import requests
import argparse

def main(url: str, file: str = None):
    print(f"Fetching data from {url}...")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meta = digest(data)
        schema = build(meta=meta, schema=read(file=file) if file else {})
        write(schema=schema, file=file) if file else display(schema=schema)
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str)
    parser.add_argument("--file", type=str)
    args = parser.parse_args()

    main(url=args.url, file=args.file)