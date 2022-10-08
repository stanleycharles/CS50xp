# Version 1

import random

coin = random.choice(["heads", "tails"])
print(coin)

# Version 2

from random import choice

coin = choice(["heads", "tails"])
print(coin)

# Version 3

import random

number = random.randint(1, 10)
print(number)

# Version 4

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)








