# Version 1

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}" 
print(f"hello, {name}")

# Version 2

import re 

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), (.+)$, name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

# Version 3

import re 

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$, name)
if matches:
    last = matches.groups(1)
    first = matches.groups(2)
    name = f"{first}{last}"
print(f"hello, {name}")


# Version 4

import re 

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$, name)
if matches:
    name = matches.group(2) + "" "" + matches.group(1)
print(f"hello, {name}")


# Version 5

import re 

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$, name)
if matches:
    name = matches.group(2) + "" "" + matches.group(1)
print(f"hello, {name}")


# Version 6

import re 

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$, name)
if matches:
    name = matches.group(2) + "" "" + matches.group(1)
print(f"hello, {name}")


# Version 7

import re 

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$, name):
    name = matches.group(2) + "" "" + matches.group(1)
print(f"hello, {name}")


# Version 8

import re 

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$, name):
    name = matches.group(2) + "" "" + matches.group(1)
print(f"hello, {name}")