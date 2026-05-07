salom = "Hello World"

print(salom)

a = 30
print(a)

b = 25
print(b)
uzgarish = "Bugun biz Pythonning foundation qismini urgandik "
print(uzgarish)

# Dunder __builtins__, __init__
message = "Python: Everything is object"
print(message)

result = type(message)
print("result:", result)

'''
In Pythonm, there are builtin tools;
(1) Types  int float str list dict
(2) Functions > print() len() input() typee() str() int()
(3) Constants > Trues False None 
'''

print(dir(__builtins__))
