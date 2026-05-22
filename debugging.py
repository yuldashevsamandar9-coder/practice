''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging

'''
import random
import turtle
print("=============   Python Packages & Core Package=============")
''' PYThon Packages/Modules: Core, File and External'''  # jsda package emas Library deyiladi
# Core Packeges > https: // docs.python.org/3/library


# Core packages

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)
# turtle.done()

# ochilgan faylni albatta yopish kerak
my_file = open(
    "material/message.text",)

try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

 # with - faylni ozi yopadi
with open("material/message.text", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("with bn ochgan faylimizni yopsak bularkan")


t = turtle.Turtle()
t.shape("turtle")
t.speed(2)  # Chizish jarayonini bemalol tomosha qilishingiz uchun

# 1. TESLA LOGOTIPI (T-harfi shakli)
t.color("red")
t.pensize(5)

# T-harfining tepadagi yoyi
t.penup()
t.goto(-50, 100)
t.pendown()
t.circle(-50, -60)  # Chap yoy

t.penup()
t.goto(0, 100)
t.pendown()
t.circle(50, 60)  # O'ng yoy

# T-harfining asosiy pastga tushuvchi qismi
t.penup()
t.goto(0, 100)
t.pendown()
t.goto(0, 20)
t.goto(-10, -10)
t.goto(0, 20)
t.goto(10, -10)

# 2. TESLA CYBERTRUCK (Futuristik mashina shakli)
t.color("gray")
t.pensize(3)

# Mashinaning pastki qismi va g'ildiraklari
t.penup()
t.goto(-150, -100)
t.pendown()

t.forward(50)   # Old tomoni
t.circle(20)    # Old g'ildirak
t.forward(100)  # Kuzovning o'rtasi
t.circle(20)    # Orqa g'ildirak
t.forward(50)   # Orqa tomoni

# Mashinaning futuristik o'tkir burchakli tomi
t.left(90)
t.forward(40)   # Orqa bamper
t.left(45)
t.forward(120)  # Tomga ko'tarilish (cho'qqi)
t.left(90)
t.forward(120)  # Kapotga tushish
t.goto(-150, -100)  # Boshlang'ich nuqtaga qaytib yopish

# Toshbaqani chetga olib turamiz
t.penup()
t.goto(150, -150)

turtle.done()
