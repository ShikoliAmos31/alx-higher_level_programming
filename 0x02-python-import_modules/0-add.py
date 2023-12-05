#!/usr/bin/python3
if __name__ == "__main__":
    try:
        from add_0 import add
    except ImportError:
        print("Module 'add_0' not found. Make sure the file exists and the name is correct.")
    else:
        a = 1
        b = 2


        # The variables 'a' and 'b' should be defined outside the 'else' block
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
