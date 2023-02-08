# define the functions needed: add, sub, multi, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiple(a, b):
  answer = a * b
  print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def divide(a, b):
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
  print(" - Calculator - ")
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")

  choice = str(input("Input the letter of the operation you would like to perform: "))

  if choice == "a" or choice == "A":
    print("-- Addition --")
    a = int(input("Input your first number: "))
    b = int(input("Input your second number: "))
    add(a, b)
  elif choice == "b" or choice == "B":
    print("-- Subtraction --")
    a = int(input("Input your first number: "))
    b = int(input("Input your second number: "))
    sub(a, b)
  elif choice == "c" or choice == "C":
    print("-- Multiplication --")
    a = int(input("Input your first number: "))
    b = int(input("Input your second number: "))
    multiple(a, b)
  elif choice == "d" or choice == "D":
    print("-- Division --")
    a = int(input("Input your first number: "))
    b = int(input("Input your second number: "))
    divide(a, b)
  elif choice == "e" or choice == "E":
    print("Exiting...")
    quit()