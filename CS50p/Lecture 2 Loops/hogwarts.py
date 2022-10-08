#lists

#Version 1

students = ["Hermione", "Harry", "Ron"]

#Version 2

# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

#Version 3 - len

# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students):
#     print(i + 1, students[i])

#Version 4 - dict

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses= ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#Version 5 - dict

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

#Version 6 - dict
 o
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(students, students[student], sep=", ")

#Version 6 - dict / list / none

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "0tter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")