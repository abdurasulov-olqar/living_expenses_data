import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    f = open(file_path).read()
    name = list(json.loads(f).keys())
    value = list(json.loads(f).values())

    return name[value.index(min(value))]

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
