# Version 1

# import sys

# print("hello, my name is", sys.argv[1])
# #print("hello, my name is", sys.argv[0])

# Version 2

# import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# Version 3

# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])


# Version 4

import sys

# # check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# # Print name tags
#     print("hello, my name is", sys.argv[1])


# Version 5

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

#     print("hello, my name is", sys.argv[1])

# Version 6

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv:
    print("hello, my name is", arg)

# Version 7

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)
    
# Version 8

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)





