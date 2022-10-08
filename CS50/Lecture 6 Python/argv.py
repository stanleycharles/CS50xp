# Version 1

from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")

# Version 2

from sys import argv

for arg in argv:
    print(arg)

# Version 3

from sys import argv

for arg in argv[1:]:
    print(arg)

# Version 3

from sys import argv

for arg in argv[:-1]:
    print(arg)


