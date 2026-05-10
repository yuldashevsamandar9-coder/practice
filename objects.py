'''
OBJECTS
(1) What is object
(2) Iterable objects & Range
(3) Dictionary
(4) Error handling system

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
# OOP 4 Concepts > Abstraction | Encapsulation | Inheritence | Polimorphism

# Call Define qismi math methodini ichiga tahlab berilgan oldindan
result1 = math.ceil(97.7)
print("result1:", result1)

result2 = ceil(99.1)
print("result2:", result2)

result3 = ceil(0.9)
print("result3:", result3)

result4 = ceil(31.2)
print("result4 :", result4)

print("=====  Error handling system =======")
car_dict = dict(name="Toyota", years=2026, electric=True, speed=220)

try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")
print("==== Test3 ======")
try:
    print("passed here")
    result = car_dict["years"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")

print("==== Test2 ======")
try:
    print("passed here")
    result = car_dict["speed"]

    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")
