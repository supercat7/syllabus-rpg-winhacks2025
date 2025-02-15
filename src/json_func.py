import json
import os

datapath = "./data/comp.json"
# receives a dictionary of course components and corresponding weights
def write_comp_to_json(comp_dict):
    with open(datapath, "w") as j:
        json.dump(comp_dict, j)

# returns dictionary from json file
def read_json():
    with open(datapath, "r") as j:
        data = json.load(j)
        j.close()
        return data

def write_grade_to_json(comp, grade):
    with open(datapath, "r") as j:
        data = json.load(j)
        data[comp]["Grade"] = grade

    with open(datapath, "w") as j:
        json.dump(data, j, indent=4)


# data = {
#     "Final": {
#         "Weight": "100",
#         "Grade": ""
#         }
#     }
# 
# write_comp_to_json(data)
# print(read_json())  
# write_grade_to_json("Final", "75")
# print(read_json())