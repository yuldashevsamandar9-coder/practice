'''
CLASS
(1) What is class
(2) Ordinary vs static properties
(3) spicial/ magic methods

'''
print("=====  What is class =======")
# class - shablon
# structure > state constructor method


class Person():

    message = "static state property"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Bu metodlar __init__ dan tashqarida, lekin klass ichida
    def introduce(self):
        print(f"{self.name} says: How do you do")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed")


# Bu qism butunlay klassdan tashqarida (chapda)
person1 = Person("Leo", 22)
person2 = Person("Neo", 29)
person3 = Person("Sem", 29)

# ordinary state
print("person1.name:", person1.name)
print("person2.name:", person2.name)
print("person3.name:", person3.name)

# oridinary method

person1.introduce()
person1.say_age()


print("=====  Ordinary vs static properties =======")
# static state


new_message = Person.message
print("new_message:", new_message)

# static method

Person.explain()


print("=====  Special magic method =======")
# Pythonning eng ishlatiladigan methodlari
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car:
    description = "This class makes cars"

    def __new__(cls, *args, ):
        print("*__new__* ")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("*__init__* ")

    def start_engine(self):
        print(f"the {self.name} started engine")

    def stop_engine(self):
        print(f"the {self.name} stopped engine")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year"

    def __call__(self):
        return f"{self.name} is being called!"


my_car = Car("Ferrari", 2026)
my_car.start_engine()


your_car = Car("Toyota", 2025)
print(your_car)


response = your_car()
print("response:", response)
