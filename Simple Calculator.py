"""
Project: Calculator
Goal: Create a simple calculator that takes 2 integers from the user and calculates a result using the add, subtract, multiply, and divide operators.
"""
num1 = int(input("please enter a number"))
num2 = int(input("please enter a second number"))

calclist = ["space", "add", "subtract","multiply","divide"]
operation = input("which operation do you want. enter vaue from 1-4, the options are...add,subtract,multiply,divide")
calclist == operation

if (int(operation) == 1):
  output = num1 + num2
  print(output)
elif (int(operation) == 2):
  output = num1 - num2
  print(output)
elif (int(operation) == 3):
  output = num1 * num2
  print(output)
elif (int(operation) == 4):
  output = num1/num2
  print(output)