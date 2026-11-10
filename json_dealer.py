import json

def get_json():
    with open("library.json", "r") as file:
        loads = json.load(file)
    return loads

def add_to_json(book):
    loads = get_json()
    loads.append(book)
    with open("library.json", "w") as file:
        json.dump(loads, file, indent=2)
    return "added successfully"


def update_json(full_list):
    with open("library.json", "w") as file:
        json.dump(full_list, file, indent=2)
    return "added successfully"




