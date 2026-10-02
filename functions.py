# Basic syntax of a function:
#
# def function_name(parameters):
#     statements
#     return value
# A function with no parameters and no return value

def sayHello():
    print("Hello, students!")
    print("Welcome to Computer Science")

# Calling the function
sayHello()


# A function with one parameter

def greet(name):
    print("Hello", name)

greet("Ali")
greet("Sara")
greet("Ahmed")


# A function that takes two numbers
# and returns their sum
#0 and 20 are hard-coded arguments

def addNumbers(num1, num2):
    total = num1 + num2
    return total

answer = addNumbers(10, 20)

print("Answer:", answer)



def addNumbers(num1, num2):
    total = num1 + num2
    return total

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

def swap(numbers):
    temp = numbers[0]
    numbers[0] = numbers[1]
    numbers[1] = temp

numbers = [10, 20]

swap(numbers)

print(numbers)

answer = addNumbers(number1, number2)

print("Answer:", answer)
