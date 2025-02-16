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
    for i in range(len(new_data)):
        new_data[i]["Grade"] = None
    print(new_data)

    data = read_json()    
    data.append(new_data)
    
    with open(datapath, 'w') as file:
        json.dump(data, file, indent=4)

def get_assignment_by_name(course_name):
    data = read_json()
    for assignment_group in data:
        for assignment in assignment_group:
            if assignment.get("Assignment") == course_name:
                return assignment
    return None

def load_all_assignments():
    assignments_dict = {}
    
    for assignment_group in data:
        for assignment in assignment_group:
            assignment_name = assignment.get("Assignment")
            assignments_dict[assignment_name] = assignment  # Add to the dictionary
            
    return assignments_dict
