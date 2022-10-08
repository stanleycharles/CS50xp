# Version 1

from cs50 import get_string

people = {
    "Cartier": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")


# Version 2

import csv
from cs50 import get_string

file open("phonebook.csv", "a")

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file)
write.writerow([name, number])

file.close()


# Version 3

import csv
from cs50 import get_string

name = get_string("Name: ")
number = get_string("Number: ")

with open("phonebook.csv", "a") as file:

    writer = csv.writer(file)
    write.writerow([name, number])


