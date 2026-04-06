def digest(data: dict | list, path: str = "", meta: dict = {}):
    """Flattens each object in the API response into a dictionary object containing {path: details}."""
    if isinstance(data, dict):
        for k, v in data.items():
            meta[f"{path}{k}"] = {"path": path if path else None, "type": type(v).__name__}
            if isinstance(v, (dict, list)):
                digest(data=v, path=f"{path}{k}/", meta=meta)
            else:
                meta[f"{path}{k}"].update({"example": v})

    elif isinstance(data, list):
        for v in data:
            digest(data=v, path=path, meta=meta)

    return meta

def build(meta: dict, schema: dict = {}):
    """Loops through the flattened API response data that was created by the digest function."""
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