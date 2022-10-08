# Version 1

from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0: 
        break
    
for i in range(n):
    print("#")


# Version 2

from cs50 import get_int

def(main):
    height = get_height()
    for i in range(height):
        print("#")


def get_height(): 
    while True:
        n = get_int("Height: ")
        if n > 0: 
            break
    return n

main()


# Version 3

from cs50 import get_int

def(main):
    height = get_height()
    for i in range(height):
        print("#")

def get_height(): 
    while True:
        try:
        n = int(input("Height: "))
        if n > 0: 
            brea5
    except ValueError:
        print("Thats not an integer!")
    return n

main()


# Version 4

from i in range(4):
    print("?", end="!!!")
print()

# Version 5

from i in range(4):
    print("?", end="\n")
print()

# Version 6

from i in range(4):
    print("?" * 4)

# Version 7

from i in range(3):
    for j in range(3):
        print("#", end="")
    print()

from i in range(3):
     print("#" * 3)







