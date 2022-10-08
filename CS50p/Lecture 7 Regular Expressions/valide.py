# Version 1

email = input("What's your email ?").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")


# Version 2


email = input("What's your email ?").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")


# Version 3


email = input("What's your email ?").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    Print("Invalid")


# Version 4


email = input("What's your email ?").strip()

username, domain = email.split("@")

if username and domain.endwith(".edu"):
    print("Valid")
else:
    Print("Invalid")


# Version 5

import re

email = input("What's your email ?").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")


# Version 6

import re

email = input("What's your email ?").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")


# Version 7

import re

email = input("What's your email ?").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")


# Version 8

import re

email = input("What's your email ?").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")


# Version 9

import re

email = input("What's your email ?").strip()

if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")


# Version 10

import re

email = input("What's your email ?").strip()

if re.search(".+@.+.edu", email):
    print("Valid")
else:
    print("Invalid")


# Version 11

import re

email = input("What's your email ?").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")


# Version 12

import re

email = input("What's your email ?").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Version 13

import re

email = input("What's your email ?").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Version 14

import re

email = input("What's your email ?").strip()

if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Version 15

import re

email = input("What's your email ?").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Version 16

import re

email = input("What's your email ?").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")


# Version 17

import re

email = input("What's your email ?").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# Version 18

import re

email = input("What's your email ?").strip()

if re.search(r"^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# Version 19

import re

email = input("What's your email ?").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# Version 20


import re

email = input("What's your email ?").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")












