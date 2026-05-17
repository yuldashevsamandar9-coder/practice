# '''
# Tuple
# (1) What is tuple: typle vs list
# (2) Unpacking arguments
# (3) zip

# '''

print("======  What is tuple: typle vs list ======")
# Java / PHP / NodeJS array => Python list,

# literal
numbs = [3, 5, 6, 7]
car_dict = {"brand": "Ferrari", "year": 1996}
print(numbs)


# constructor
letters = list("Hello World!")
person_dict = dict(name="SAM", AGE=29)
print(letters)


fruits = ["apple", "banana", "kiwi"]
print(fruits)
fruits[1] = "nok"
print(fruits)

# tuple
# we can not mutate tuple

animals = ("dog", "cat", "fish")
typle_obj = ("MIT", 100, True)
print(animals[0])
# animals[0] = "bird"

print("======  Unpacking arguments ======")
groups = ["MIT", "FLEXY", "DEVEX", "MG", "MIT39"]
(x, y, z, s, f) = groups
print(f"the x: {x} and y: {y}  and s: {s}")
print("z: ", z)
# args tuple


def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total += x
    print(f"the total value: {total}")
    return total


# CALLL
calculate(7, 3, 40, 5)
calculate(7, 3)
calculate(7, 20)


def introduce(**kwargs):
    print("the type:(**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and I am {kwargs["age"]}years old!")


# Call
introduce(name="Justin", age=25)
# introduce(name="SAM", age=29, single=True)
# introduce(name="Leo", age=22, )


def greeting(*args, **kwargs):
    print("*args>", args)
    print("**kwargs>", kwargs)


greeting("Hi", True, 10, name="Neo", age=29)

print("======  zip ======")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
result = list(zipped)
print(f"the result: {result}")
print("--------")
