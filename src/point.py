import json_func
datapath = "./data/points.json"

def grade_to_point(grade, weight):
    return (grade * weight) / 10

def get_point():
    with open("points.json", "r") as file:
        data = json.load(file)
        return data["Points"]

def set_point(point):
    with open(datapath, "r") as j:
        data = json.load(j)
        data["Points"] = point

    with open(datapath, "w") as j:
        json.dump(data, j, indent=4)


write_comp_to_json(data)
print(read_json())  
write_grade_to_json("Final", "75")
print(read_json())