import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="sports.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    equipment = list(reader)

print("All Sports Equipment:")
for item in equipment:
    print(item)

eid = input("Enter Equipment ID to search: ")

found = False

for item in equipment:
    if item["Equipment ID"] == eid:
        print("Equipment Found:")
        print(item)
        found = True
        break

if not found:
    print("Equipment not found")
