# Version 1

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS)
            print("meow")

cat = Cat()
cat.meow()


# Version 2


def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)


# Version 3

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = input(input("Number: "))
meow(number)


# Version 4

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = input(input("Number: "))
meows: str = meow(number)
print(meows)


# Version 4

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = input(input("Number: "))
meows: str = meow(number)
print(meows)


# Version 5

def meow(n: int) -> str:
    return "meow\n" * n

number: int = input(input("Number: "))
meows: str = meow(number)
print(meows, end="")


# Version 6

def meow(n: int) -> str:
    """Meow n Times."""
    return "meow\n" * n

number: int = input(input("Number: "))
meows: str = meow(number)
print(meows, end="")


# Version 7

def meow(n: int) -> str:
    """
    Meow n Times.
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str

    """
    return "meow\n" * n

number: int = input(input("Number: "))
meows: str = meow(number)
print(meows, end="")


# Version 8

import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")

# Version 9

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")


# Version 10

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")


# Version 11

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")


# Version 12

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")








    