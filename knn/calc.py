def multiply(x ,y):
   i = x * y
   return i
def power(x, y):
   i = x ** y
   return i
def divide(x ,y):
   i = x / y
   return i
def add(x ,y):
   i = x + y
   return i
def subtract(x ,y):
   i = x - y
   return i
operation = input("add, subtract, multiply,power, or divide")
if operation == "add":
   add1 = float(input("add first number: "))
   add2 = float(input("add second number: "))
   print(add(add1, add2))
if operation == "subtract":
   subtract1 = float(input("first number: "))
   subtract2 = float(input("subtract second number "))
   print(subtract(subtract1, subtract2))
if operation == "multiply":
   multiply1 = float(input("first number: "))
   multiply2 = float(input("multiply second number "))
   print(multiply(multiply1, multiply2))
if operation == "divide":
   d1 = float(input("first number: "))
   d2 = float(input("divide second number "))
   print(divide(d1, d2))
if operation == "power":
   subtract1 = float(input("first number: "))
   subtract2 = float(input("subtract second number "))
   print(power(subtract1, subtract2))