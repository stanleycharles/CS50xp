# Version 1

print("meow")
print("meow")
print("meow")

# Version 2

for i in range(3):
    print("meow")
    
# Version 3

def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

if __name__ == "__main__":
main()


# Version 4

def main():
    for i in range(3):
        meow()

def meow():
    print("meow")

main()

# Version 5

def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")
main()




