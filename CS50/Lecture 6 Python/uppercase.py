# Version 1

from cs50 import get_string

before = get_string(Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(), end="")
print()


# Version 2

from cs50 import get_string

before = get_string(Before: ")
print(f"After: {before.upper()}")