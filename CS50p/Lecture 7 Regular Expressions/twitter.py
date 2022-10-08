# Version 1

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# Version 2

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")


# Version 3

import re

url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}")


# Version 4

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)twitter\.com/", "", url)
print(f"Username: {username}")


# Version 5

import re

url = input("URL: ").strip()

re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))

# Version 6

import re

url = input("URL: ").strip()

re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))


# Version 7 

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    print(f"Username:", matches.group(1))


# Version 8

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE)
    if matches.group(1) == "com":
        print(f"Username:", matches.group(1))


# Version 8

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
        print(f"Username:", matches.group(1))


