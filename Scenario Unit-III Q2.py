import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="employee.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

print("All Employee Records:")
for emp in employees:
    print(emp)

eid = input("Enter Employee ID to search: ")

found = False

for emp in employees:
    if emp["Employee ID"] == eid:
        print("Employee Found:")
        print(emp)
        found = True
        break

if not found:
    print("Employee not found")
