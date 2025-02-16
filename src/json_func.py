import json
import os

datapath = "./data/comp.json"
# receives a dictionary of course components and corresponding weights
def write_comp_to_json(data):
    try:
        # Assuming you are writing to the JSON file
        with open(datapath, 'r+') as f:
            current_data = json.load(f)
            current_data.update(data)
            f.seek(0)
            json.dump(current_data, f, indent=4)
    except Exception as e:
        print(f"Error writing to JSON: {e}")
        raise


# returns dictionary from json file
def read_json():
    try:
        with open(datapath, "r") as j:
            data = json.load(j)
        return data
    except FileNotFoundError:
        return {}  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        return {}  # Return an empty list if the file isn't valid JSON


def write_grade_to_json(comp, grade):
    data = read_json()
    data[comp]["Grade"] = grade

    with open(datapath, "w") as j:
        json.dump(data, j, indent=4)
        j.close()

def get_comp_grade(comp):
    data = read_json()
    return data[comp]["Grade"]

def get_comp_date(comp):
    data = read_json()
    return data[comp]["Date"]