# About
Small python CLI tool to automatically generate a simple API schema.

## Usage
Make sure your `domain` is correct and complete, containing any versioning or other API details like `api.domain.com/v1` if applicable. Only the `domain` and `endpoint` arguments are required. 

**Call Without Params**
```bash
python main.py --'domain.com' --endpoint='endpoint/etc'
```

**Call With Params**
multiple parameters can be used if they are comma-separated within the dictionary string
```bash
python main.py --'domain.com' --endpoint='endpoint/{key}/etc' --params='{"key": "value"}'
```