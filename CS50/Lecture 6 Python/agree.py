# Version 1

from cs50 import get_string

s = get_string("Do you agree ?")

if s == "Y" or s == "y":
    print("Agreed.")
elif s == "N" or s == "n":
    print("Not agreed.")



# Version 2

from cs50 import get_string

s = get_string("Do you agree ?")

if s in ["Y", "y", "yes"]:
    print("Agreed.")
elif s in ["N", "n", "no"]
    print("Not agreed.")

# Version 3

from cs50 import get_string

s = get_string("Do you agree ?")

if s.lower() in ["y", "yes"]:
    print("Agreed.")
elif s.lower in ["n", "no"]
    print("Not agreed.")


# Version 4

from cs50 import get_string

s = get_string("Do you agree ?").lower()

if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]
    print("Not agreed.")