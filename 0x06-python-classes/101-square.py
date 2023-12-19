#!/usr/bin/python3
def my_print(self):
    """
    Prints the square using the character #.
    """
    if self.__size == 0:
        print()
        return

    for _ in range(self.__position[1]):
        print()

    for _ in range(self.__size):
        print(" " * self.__position[0] + "#" * self.__size)
