'''
List 
(1) Working with lists
(2) List method
(3) Lambda function
(4) enumerate, map and filter

'''
print("====== Working with lists =========")
# Java / PHP / NodeJS array => Python list,

# literal

person = {"name": "Justin", "age": 25}  # dictinary
person = ("Andrew", "JOhn", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")

# constructor
result = list("Hello World")
print(f"the result: {result} and size: {len(result)}")

print("-------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0.2]
c = fruits[:: 3]
d = fruits[:: -1]


print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("====== list methods =========")
# methods > append(), insert(), pop(), reverse(), clear(), sort(), index()

letters = ["a", "d", "b"]
letters.append("c")  # oxiridan qushdi
print(f"the insert letters: {letters}")


size = len(letters) - 1
result1 = letters.pop(size)  # pop
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)
print(f" the pop result2: {result2} and letters: {letters}")

print("-----")
animals = ["dog", "cat", "fish", "capybara"]
print("animals:", animals)

animals.remove("capybara")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

# animals.clear()
# print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("-------")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutale > sorted function & index() method
numbs1 = [2, 20, 12, 100]
new_numbs = sorted(numbs1)
print(f"the sorted numbs1: {numbs1} and new_numbs: {new_numbs}")

print("====== Lambda function =========")
# Lambda is small anonyms function!


def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 26),
    ("Michael", 30),
    ("ALi", 40)
]
people.sort()
print("people(1)", people)

people.sort(key=lambda person: person[1])
print("people(2)", people)

print("====== enumerate, map and filter =========")
# enumereate for index & value

animals = ["dog", "cat", "fish"]  # list
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value:  {value} ")
    print("--------")
    car_obj = dict(brand="Ferrari", year=2005)  # dict
    result = car_obj.items()
    for (key, value) in result:
        print(f"the key: {key} and value: {value}")
        print("--------")
    # map
    cars = [
        ("Ferrari", 78),
        ("Tayoto", 87),
        ("Audi", 110),
        ("BWM", 109),
        ("Pagani", 33)
    ]
    new_cars = []
for car in cars:
    new_cars.append(car[0])
    print("new_car:", new_cars)

    result1 = map(lambda car: [0], cars)
    print(f"result1: {result1} and type: {type(result1)} ")
    print("-----")
    # filter
    result_filter = filter(lambda car: car[1] > 80, cars)
    print(
        f"the result_filter: {result_filter} and type: {type(result_filter)}")
    print(list(result_filter))
