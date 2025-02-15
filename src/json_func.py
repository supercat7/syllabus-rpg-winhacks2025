import json
import os

datapath = "./data/comp.json"
# receives a dictionary of course components and corresponding weights
def write_to_json(comp_dict):
    with open(datapath, "w") as j:
        json.dump(comp_dict, j)

# returns dictionary from json file
def read_json():
    with open(datapath, "r") as j:
        data = json.load(j)
        j.close()
        return data

def remove_from_json(comp):
    
dat = {"Hello": "1", "World": "2"}
write_to_json(dat)
print(read_json())
remove_from_json("Hello")
print(read_json())

