print("===== numbeer======")
# In Java variable is a name storage location!
# In Python, variable is named reference

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # Method

result2 = count.numerator  # state
print(result1, result2)

print("===== string ====")
# Methods : upper() lower() title() find() replace()

course = "AI Python Fullstack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

result = course.upper()
print(f"the result (3): {result}")


result = course.replace("Fullstack", "MasterClass")
print(f"the result (4): {result}")


print("===== boolean ====")

# Functions > type() input() bool() int() str()

y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f" the input value isnumeric: {result}")

# TRUTHY VS FALSY value
# TRUTHY > true 100 -100 "Sem"
#  FALSY > false 0 "" None

test_falsy = ""
print("The Falsy:", bool(test_falsy))

test_truthys = "Sem"
print("The Falsy:", bool(test_truthys))
