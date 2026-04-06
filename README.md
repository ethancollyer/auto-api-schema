# About
Small python CLI tool to automatically generate a simple API schema.

## Usage
Make sure your `domain` is correct and complete, containing any versioning or other API details like `api.domain.com/v1` if applicable. You can both save the schema and source an existing schema using the optional `--file` argument.

| Argument | Required |  Type  |          Description          |
|----------|----------|--------|-------------------------------|
| url      | True     | String | URL to the desired endpoint.  |
| file     | False    | String | File to use as both the source input and target output for the schema. Only requires a file name and uses the working directory by default. Can include the complete path or relative path if desired. |

**Call Without File**
```bash
python main.py 'https://domain.com/v1/endpoint/etc?params={param}'
```

**Call With File**
```bash
python main.py 'https://api.domain.com/v1/endpoint/etc' --file='schema.json'
```