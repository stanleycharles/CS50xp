#Version 1

# from cs50 import get_int

# x = get_int("x: ")
# y = get_int("y: ")
# print(x + y)


# Version 2

# from cs50

# x = cs50.get_int("x: ")
# y = cs50.get_int("y: ")
# print(x + y)

# Version 3

# from cs50

# x = int(input("x: "))
# y = int(input("y: "))
# print(x + y)

# Version 3

try:
    x = int(input("x: "))
except:
    print("That is not an int!")
    exit()
try:
    y = int(input("y: "))
except:
    print("That is not an int!")
    exit()
print(x + y)


# Version 4

try:
    x = int(input("x: "))
except ValueError:
    print("That is not an int!")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!")
    exit()
print(x + y)


# Version 5

from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

z = x // y
print(z)


# Version 6

from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

z = x / y
print(f"{z:.50f}")