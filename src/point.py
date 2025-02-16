import json

datapath = "./data/points.json"

def grade_to_point(grade, weight):
    return (grade * weight) / 10

def get_point():
    with open(datapath, "r") as file:
        data = json.load(file)
        return data["Points"]

def set_point(point):
    with open(datapath, "r") as j:
        data = json.load(j)
        data["Points"] = point

    with open(datapath, "w") as j:
        json.dump(data, j, indent=4)

def set_level(level):
    with open(datapath, "r") as j:
        data = json.load(j)
        data["Level"] = level
    with open(datapath, "w") as j:
        json.dump(data, j, indent=4)

def update_level():
    point = get_point()
    level = round(int(point) / 100)
    set_level(level)