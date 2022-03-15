import json

with open("data.json","r") as data_file:
    data  = json.load(data_file)
print(data)
print(data["kj"]["password"])