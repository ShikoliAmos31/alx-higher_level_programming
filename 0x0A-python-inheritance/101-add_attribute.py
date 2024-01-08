#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    """Add attribute to object if the object is mutable."""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
