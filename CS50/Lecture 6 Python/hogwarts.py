# Version 1

import csv

houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

with open("hogwarts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        house = row[1]
        houses[house] += 1

for house in houses:
    count = houses[house]
    print(f"{house}: {count}")

# Version 2

import csv

houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

with open("hogwarts.csv", "r") as file:
    reader = csv.Dictreader(file)
    for row in reader:
        house = row["House"]
        houses[house] += 1

for house in houses:
    count = houses[house]
    print(f"{house}: {count}")