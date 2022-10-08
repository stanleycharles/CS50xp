# Version 1

first, last = input("What's your name? ").split(" ")
print(f"hello, {first}")

# Version 2

first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")

# Version 3

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(100, 50, 25), "Knuts")

# Version 3

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")


# Version 4

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")

# Version 5

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# Version 6

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# Version 7

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

# Version 8

def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25, 5)

# Version 9

def f(*args, **kwargs):
    print("Named:", args)

f(galleons=100, sickles=50, knuts=25)

# Version 10

def print(*objects, sep=" ", end="\n", ...):
    for object in objects:
        ...

# Version 11

def print(*objects, sep=" ", end="\n", ...):
    for object in objects:
        ...


