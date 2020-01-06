# your code goes here...
import math
def ints_only(inp):
    if isinstance(inp, int):
        print("{} is an integer".format(inp))
    else:
        print("{} is not an integer".format(inp))
# DO NOT CHANGE THIS CODE
inp = input("Input a number: ")
ints_only(inp)