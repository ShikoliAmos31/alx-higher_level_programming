#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints the message "My name is <first_name> <last_name>"

    :param first_name: The first name as a string
    :param last_name: The last name as a string (default is an empty string)
    :raises TypeError: If either first_name or last_name is not a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = f"My name is {first_name} {last_name}".strip()
    print(full_name)

# Example usage
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")

# Example of raising a TypeError
try:
    say_my_name(12, "White")
except TypeError as e:
    print(e)
