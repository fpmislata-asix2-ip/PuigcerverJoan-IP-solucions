with open("ud5/files/data/exemple.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        print(l)

import csv
print("CSV")
with open('ud5/files/data/exemple.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

import json
print("JSON")
with open('ud5/files/data/exemple.json', 'r') as file:
    data = json.load(file)
    print(data)

import yaml
print("YAML")
with open('ud5/files/data/exemple.yml', 'r') as file:
    data = yaml.safe_load(file)
    print(data)


modul = {
    "name": "Introducció a programació",
    "hores": 96,
    "teacher": "Joan Puigcerver"
}
with open('ud5/files/data/modul.json', 'w') as file:
    json.dump(modul, file, indent=4)