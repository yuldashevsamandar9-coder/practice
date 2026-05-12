'''
Class deep diving
(1) Encapsulation
(2) Inheritence
(3) Polimorhism

'''

print("===== Inheritence =======")


class Animal():  # Parent
    description = "This class is parent for animals"

    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


class Dog(Animal):  # Child

    def __init__(self, name, voice, sound, ):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.voice} - {self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):  # Child

    def __init__(self, name, voice, sound, ):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.voice} - {self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child

    def __init__(self, name, voice, sound, ):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.voice} - {self.sound}")

    def swim(self):
        print("Yes, I can swimming")


dog = Dog("Simbo", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nano", "zzzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()
print("--------")

dog.make_voice()
cat.make_voice()

print("--------")
print("====== Polymorpysim=====")

dog.make_voice()
cat.make_voice()


# fish > Fish > Animal > Object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
result = a and b and c
print(f"the result:", {result})
