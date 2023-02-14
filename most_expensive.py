import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f = open(file_path).read()
    name = list(json.loads(f).keys())
    value = list(json.loads(f).values())

    return name[value.index(max(value))]

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)