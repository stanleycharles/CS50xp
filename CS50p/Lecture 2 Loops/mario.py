#Version 1 - Nested loops

for _ in range(3):
    print("#")

#Version 2

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

#Version 3

def main():
    print_row(4)

def print_row(width):
        print("?" * width)

main()

#Version 4

def main():
    print_square(3)

def print_square(size):
        for i in range(size): #for each row in sq
            for j in range(size): #for each brick in row
                print("#", end="")
            print()

main()

#Version 5

def main():
    print_square(3)

def print_square(size):
        for i in range(size): #for each row in sq
                print("#" * size)

main()

#Version 6

def main():
    print_square(3)

def print_square(size):
        for i in range(size): l
                print_row(size)

def print_row(width):
    print("#" * width)

main()


