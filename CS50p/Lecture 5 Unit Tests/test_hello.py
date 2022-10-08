from hello import hello

def test_defaut():
   assert hello == "hello, world"

def test_argument():
   assert hello("David") == "hello, David"

def test_argument():
   for name in ["Hermione", "Harry", "Ron"]:
         assert hello(name) == f"hello, {name}"

