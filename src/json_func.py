import json
import os

datapath = "./data/comp.json"
# receives a dictionary of course components and corresponding weights
def write_comp_to_json(comp_dict):
    with open(datapath, "w") as j:
        json.dump(comp_dict, j)
        j.close()

# returns dictionary from json file
def read_json():
    with open(datapath, "r") as j:
        data = json.load(j)
        j.close()
        return data

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