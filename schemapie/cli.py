from schemapie.utils.api import execute
import argparse

def main():
    parser = argparse.ArgumentParser(prog="schemapie")
    parser.add_argument("url", type=str, help='Complete URL of the desired API route.')
    parser.add_argument("--file", type=str, help='File name or path. Used to create reusable schemas, update existing schemas, or just to save a schema.')
    args = parser.parse_args()

    execute(url=args.url, file=args.file)