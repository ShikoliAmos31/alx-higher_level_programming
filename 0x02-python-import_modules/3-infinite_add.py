#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    result = 0
    for i in sys.argv[1:]:
        try:
            result += int(i)
            print("{}".format(result))
        except valueError:
            print(f"Error: {i} is not a valid integer.")

