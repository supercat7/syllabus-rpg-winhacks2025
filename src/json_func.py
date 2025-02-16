import json
import os

datapath = "./data/comp.json"

# Ensure the data directory exists
os.makedirs(os.path.dirname(datapath), exist_ok=True)

# Initialize comp.json with an empty list if it doesn't exist
if not os.path.exists(datapath):
    with open(datapath, 'w') as file:
        json.dump([], file)

# Receives a dictionary of course components and corresponding weights
def write_comp_to_json(comp_dict):
    try:
        print(f"Writing data to {datapath}: {comp_dict}")  # Debugging
        data = read_json()
        data.append(comp_dict)
        with open(datapath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data written successfully: {data}")  # Debugging
    except Exception as e:
        print(f"Error writing to JSON: {e}")
        raise

# Returns data from json file
def read_json():
    try:
        with open(datapath, "r") as j:
            data = json.load(j)
            print(f"Data read from {datapath}: {data}")  # Debugging
            return data
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []