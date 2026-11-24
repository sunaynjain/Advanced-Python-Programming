import csv
import json

csv_file = "input.csv"
json_file = "output.json"

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV converted to JSON successfully")
