# Version 1

import csv

with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])


# Version 2

import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["title"])


# Version 3

import csv

titles = []

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if not row["title"] in titles:
            titles.append(row["title"])

for title in titles:
    print(title)

# Version 4

import csv

titles = []

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if not title in titles:
            titles.append(title)

for title in titles:
    print(title)
    


# Version 5

import csv

titles = set []

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        titles.add(title)

for title in sorted(titles):
    print(title)


# Version 6

import csv

titles = set {}

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if not title in titles:
            titles(title) = 0
        titles(title) += 1

for title in titles:
    print(title, titles(title))

# Version 7

import csv

titles = set {}

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if not title in titles:
            titles(title) = 0
        titles(title) += 1

def get_value(title):
    return titles(title) 

for title in sorted(titles, key=get_value, reverse=True):
    print(title, titles(title))


# Version 8

import csv

titles = set {}

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if not title in titles:
            titles(title) = 0
        titles(title) += 1

for title in sorted(titles, key=lambda title: titles(title), reverse=True):
    print(title, titles(title)) 


# Version 9

import csv

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if title == "THE OFFICE":
            counter += 1
print("Number of people wwho like the office: {counter}")   


# Version 10

import csv

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if "OFFICE" in title
            counter += 1

print("Number of people wwho like the office: {counter}")   

 
# Version 10

import csv
import re

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()
        if re.search("^OFFICE|THE OFFICE)$", title):
            counter += 1

print("Number of people wwho like the office: {counter}")  


# Version 11

import csv

title = input("Title: ").strip().upper()

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1

print(counter)


# Version 12 - SQL

import csv

from cs50 import SQL

db = SQL("sqlite:///favorites.db")

title = input("Title: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE title LIKE ?", title)

row = rows[0]
