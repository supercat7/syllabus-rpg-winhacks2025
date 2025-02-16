import os
import openai
import json

datapath = './data/comp.json'

def read_json():
    try:
        with open(datapath, 'r') as file:
            data = json.load(file)
            if not data:
                return []
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def append_to_json(new_data):
    data = read_json()    
    data.append(new_data)
    
    with open(datapath, 'w') as file:
        json.dump(data, file, indent=4)
    
    

# {"NAME", "DATE", WEIGHT, "GRADE"}