# Version 1

from msilib.schema import Property


name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")


# Version 2

def main():
    name = get.name()
    house = get.house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()


# Version 3

def main():
    name = get.name()
    house = get.house()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")

if __name__ == "__main__":
    main()


# Version 4

def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()

# Version 5

def main():
    n, h = get_student()
    print(f"{name} from {house}")

def get_student():
    n = input("Name: ")
    h = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()


# Version 6

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()


# Version 7

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenlaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()

# Version 8

def main():
    student = get_student()
    print(f"{student['name']} from {student['House']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House ")
    return student 

if __name__ == "__main__":
    main()


# Version 8

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] == "Ravenclaw"

    print(f"{student['name']} from {student['House']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House ")
    return {"name": name, "House":house}

if __name__ == "__main__":
    main()


# Version 9 - class

class Student:

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()


# Version 10

class Student:

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()


# Version 11

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()


# Version 12

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# Version 13

class Student:
    def __init__(self, first, middle, last, house):
        if not first:
            raise ValueError("First Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.first = first
        self.middle = middle
        self.last = last
        self.house = house 
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    first = input("First Name: ")
    middle = input("Middle Name: ")
    last = input("Last Name: ")
    house = input("House ")
    return Student(first, middle, last, house)

if __name__ == "__main__":
    main()


# Version 14

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 
   
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()



# Version 15

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 

    def __str__(self):
        return "a student"
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# Version 16

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# Version 17

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    patronus = input("Patronus ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
    

# Version 18

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "ST"
            case "Otter":
                return "OT"
            case "Jack Russell":
                return "JR"
            case _:
                return "/"
    
def main():
    student = get_student()
    print("Expecto Patronum")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House ")
    patronus = input("Patronus ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()


# Version 19

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    student.house = "Number 4, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# Version 20

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #getter
    def house(self):
        return self.house
    
    #setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.house = house 
    
def main():
    student = get_student()
    student.house = "Number 4, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# Version 21


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name") 
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house 
    
def main():
    student = get_student()
    student.house = "Number 4, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# Version 22


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name: 
            raise ValueError("Missing Name")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house 
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)

if __name__ == "__main__":
    main()


# Version 23

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

# Version 24

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house 

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

