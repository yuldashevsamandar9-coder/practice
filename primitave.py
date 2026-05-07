
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
