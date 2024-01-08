#!/usr/bin/python3
class MyInt(int):
    """A custom class inheriting from int."""

    def __eq__(self, other):
        """Override equality (==) to be inequality (!=)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality (!=) to be equality (==)."""
        return super().__eq__(other)
