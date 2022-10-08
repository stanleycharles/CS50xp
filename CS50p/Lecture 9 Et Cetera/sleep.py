# Version 1

n = int(input("What's n? "))
for i in range(n):
    print("|" * i)

# Version 2

def main()

    n = int(input("What's n? "))
    for i in range(n):
        print("|" * i)

def sheep(n):
    return "|" * n


if __name__ == "__main__":
    main()


# Version 3

def main()

    n = int(input("What's n? "))
    for i in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        flock.append("|" * i)
    return flock

# Version 4

def main()

    n = int(input("What's n? "))
    for i in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "|" * i


if __name__ == "__main__":
    main()

# Version 5

def main()

    n = int(input("What's n? "))
    for i in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "|" * i

if __name__ == "__main__":
    main()

