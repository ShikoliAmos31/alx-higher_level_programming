#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for i in range(min(x, len(my_list))):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end=' ')
                printed_integers += 1
    except IndexError:
        pass

    print()
    return printed_integers
