'''
OBJECTS
(1) What is object
(2) Iterable objects & Range
(3) Dictionary
(4) Error handling sytem

'''

import array  # package/ module
import math  # package/ module
from math import ceil

print("=====  What is object =======")
# State va Methodlariga ega bulgan property object deyiladi
# Pythonda hamma narsa object deyiladi

print(type('Hello World'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigma (Uslubiyat) > Functional programming & OOP
# OOP 4 Concepts > Abstraction  Encapsulation Inheritence Polimorphism

# Call Define qismi math methodini ichiga tahlab berilgan oldindan
result1 = math.ceil(97.7)
print("result1:", result1)

result2 = ceil(99.1)
print("result2:", result2)

result3 = ceil(0.9)
print("result3:", result3)

result4 = ceil(31.2)
print("result4 :", result4)
