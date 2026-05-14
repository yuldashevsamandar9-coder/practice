'''
Loops Operators
(1) for 
(2) break/else
(3) while 
'''

print("==== for operators =======")
# Iterable objectlarga > string dict tuple list range map filter

text = "MIT"
numbs = [10, 7, 5, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("--------")
for number in numbs:
    print(f"the number: {number}")

print("--------")
for x in range_obj:
    print(f"the element: {x}")


print("--------")
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")


print("--------")
print("==== break/else operators =======")

for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Reached break")
        break
    else:
        print("Excetud succesfully")
        break
print("++++")

print("==== while operators =======")

numb = 40
while numb > 0:
    numb -= 10
    print(f"the number equels: {numb}")
print("--------")
count = 0
while True:
    count += 1
    x = int(input("find number "))
    if x == 41:
        print(" You found number in: {count} steps")
        break
    else:
        print("Wrong try again")
