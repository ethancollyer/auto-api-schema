# About
Small python CLI tool to automatically generate a simplified API schema.

## Usage
Make sure your `domain` in the `main` function is correct and complete, containing any versioning or other API details like `api.domain.com/v1` if applicable. Only the `endpoint` argument is required. 

**Call Without Params**
```bash
python main.py --endpoint='endpoint/etc'
```

**Call With Params**
```bash
python main.py --endpoint='endpoint/{key}/etc' --params='{"key": "value"}'
```