# Version 1

def main():
    yell("This is CS50")

def yell(words):
    print(phrase.upper())

if __name__ == "__main__":
    main()

# Version 2

def main():
    yell(["This", "is", "CS50"])

def yell(words):
    print(phrase.upper())

if __name__ == "__main__":
    main()

# Version 3

def main():
    yell(["This", "is", "CS50"])

def yell(words):
    for word in words:
        print(word, end="")


if __name__ == "__main__":
    main()

# Version 4

def main():
    yell("This", "is", "CS50")

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

# Version 5

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()

# Version 6

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper()for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()

# Version 7

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper()for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()