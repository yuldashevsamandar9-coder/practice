'''
FUNCTIONS
(1) DEFINE VS CALL
(2) Parametr vs argument
(3) Keyword & default arguments
(4) Scope



'''

print("======= Define vs Call =======")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} inn Java, Pyhton uses indetation!
# Function malum bir operatsiyaniu amalga oshiradigan  kod blok Java shunday deyiladi
# Pythonda esa indentation yani orasini tashlab yozilarkan aftamatiski

# Define - parametr


def greet(a):
    print(f"Qalaysan,{a} ")


def greeting(b):
    print("greeeting is executed")
    return f"Hi {b}"

    # Call

    result1 = greet('Sem')
    print("result1:", result1)


result2 = greeting("Justin")
print("result2:", result2)


print("======= Keyword vs default arguments =======")

# Define


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# Call
result3 = give_greet(name='Justin', age=28)
print("result3:", result3)


result4 = give_greet("John")
print("result4:", result4)
