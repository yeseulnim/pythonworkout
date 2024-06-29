# for this function, you need to write a function (hex_output)
# that takes a hex number and returns the decimal equivalent.
# and no, you shouldn't convert the number all at once using the int function,
# although it's permissible to use int one digit at a time.

def hex_output():
    hexnum = input("Enter a hex number:")
    decnum = 0
    for ind, val in enumerate(reversed(hexnum)):
        decnum += int(val) * (16**ind)
    print(decnum)
    return None

#hex_output()

# reimplement the solution for this exercise
# such that it doesn't use the int function at all,
# but rather uses the built-in ord and chr functions to identify the characters.
# this implementation should be more robust,
# ignoring characters that aren't legal for the entered number base.

def hex_output2():
    hexnum = input("Enter a hex number:")
    decnum = 0
    for ind, val in enumerate(reversed(hexnum)):
        if val in ("abcdef"):
            digit = ord(val)-87
        elif 0<=int(val) and int(val)<10:
            digit = int(val)
        decnum += digit * (16**ind)
    print(decnum)
    return None

#hex_output2()

# write a program that asks the user for their name then produces a "name triangle"
# the first letter of their names, then the first two letters,
# then the first three, and so forth,
# until the entire name is written on the final line.

def name_triangle():
    name = input("Enter your name:")
    for i in range(len(name)):
        print(name[:i+1])

name_triangle()


