'''
Array & Set
(1) Array
(2) Set
(3) Specific operators with set

'''
from array import array

print("======  Array ======")

numbers = array("i", [1, 4, 5, 6, 8, 41])
print("numbers(1):", numbers)

numbers.append(200)
numbers.insert(0, 15)
print("numbers(2):", numbers)

numbers.remove(6)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)


print("======  Set ======")
# set of unique collection without keeping order!

new_numbers = array("i", [1, 4, 5, 7, 6, 7, 8, 4])
numbs_set = set(new_numbers)

print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(400)
print("numbs_set(2):", numbs_set)

numbs_set.add(70)
print("numbs_set(3):", numbs_set)


print("======  Specific operators with set ======")
# | & - ^


a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union bir xil miqdordan bittasini qabul qilarkan
result2 = a & b  # intersection Ikkala to'plamda ham bir xil elementlarni oladi
result3 = a - b  # differnce a tuplamdan b dagilarni olib tashlaydi
result4 = a ^ b  # symmertric difference umumiy bulmagan elementlarni oladi

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
