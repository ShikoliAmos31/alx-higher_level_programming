#!/usr/bin/python3
a = 10
b = 89

a = a ^ b
b = a ^ b
a = a ^ b

a, b = b, a
print("a =", a, "- b =", b)
