# Version 1

scores = [72, 73, 33]

average = sum(scores) / len(scores)
print(f"Average: {average}")

# Version 2

from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Average: {average}")


# Version 3

from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores += [score]

average = sum(scores) / len(scores)
print(f"Average: {average}")


