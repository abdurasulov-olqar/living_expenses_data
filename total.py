import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f = open(file_path).read()
    s: dict = json.loads(f).values()
    return sum(s)

# test

file_path = "data.json"
data = total_expenses(file_path)
print(data)