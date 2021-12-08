import json


def _validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except Exception:
        return False
    return True
