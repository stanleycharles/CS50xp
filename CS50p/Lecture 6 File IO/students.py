# Version 1

# with open("students.csv") as file:
#     for line in file
#       row = line.rstrip().split(",")
#       print(f"{row[0]} is in {row[1]}")


# Version 2

# with open("students.csv") as file:
#     for line in file
#       name, house = line.rstrip().split(",")
#       print(f"{name} is in {house}")


# Version 3

# with open("students.csv") as file:
#     for line in file
#       name, house = line.rstrip().split(",")
#       students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)


# Version 4

students = []

with open("students.csv") as file:
    for line in file:
      name, house = line.rstrip().split(",")
      student = {}
      student["name"] = name
      student["house"] = house
      students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# Version 5

students = []

with open("students.csv") as file:
    for line in file:
      name, house = line.rstrip().split(",")
      student = {"name": name, "house": house}
      students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# Version 6

students = []

with open("students.csv") as file:
    for line in file:
      name, house = line.rstrip().split(",")
      student = {"name": name, "house": house}
      students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

# Version 7

students = []

with open("students.csv") as file:
    for line in file:
      name, house = line.rstrip().split(",")
      student = {"name": name, "house": house}
      students.append(student)

def get_name(student):
    return student["house"]

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")


# Version 8

students = []

with open("students.csv") as file:
    for line in file:
      name, home = line.rstrip().split(",")
      student = {"name": name, "home": home}
      students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# Version 9

import csv

students = []

with open("students.csv") as file:
      reader = csv.reader(file)
      for name, home in reader:
        students.append({"name":name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# Version 10

import csv

students = []

with open("students.csv") as file:
      reader = csv.DictReader(file)
      for row in reader:
        students.append({"name":name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# Version 11

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open ("students.csv", "a") as file
    writer = csv.writer(file)
    writer.writerow([name, home])




    


    