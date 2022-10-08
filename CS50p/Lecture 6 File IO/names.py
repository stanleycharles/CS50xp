# Version 1

name = input("What's your name? ")
print(f"hello, {name}")

# Version 2

names = []

for _ in range(3):
name = input("What's your name? ")
names.append(name)

# Version 3

names = []

for _ in range(3):
names.append(input("What's your name? "))

for name sorted(names):
    print(f"hello, {name}")


# Version 4

name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()


# Version 5

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# Version 6

name = input("What's your name? ")

with open("names.txt", "a") as file:
file.write(f"{name}\n")


# Version 7

with open("names.txt", "r") 
    lines = file.readlines()
for line in lines:
    print("hello,", line.rstrip())


# Version 8

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# Version 9

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# Version 10

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# Version 11

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")










