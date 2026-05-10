print("=====  Iterable objects & RANGE  =======")
# Iterable objectlarga > string dict tuple list range map filter


range_obj = range(3)  # [0,dan 3 ga bulgan sonni oladi shunda 3 kirmaydi]
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")

    for ele in range_obj:
        print(f" the element: {ele}")

print("=====  Dictionary  =======")
# Dictionary ni Json object deb ham atarkan

person = {"name": "Sem", "age": 29, "single": False}
person_obj = dict(name="Sem", age=29, single=False)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get()
# name: person_ob["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} > value {person_obj.get(key)} ")
