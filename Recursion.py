def countDown(number):
    if number == 0:
        print("Done!")
    else:
        print(number)
        countDown(number - 1)

countDown(4)

#Python program recursive factorial function
def factorial(number):
    if number == 0:
        answer = 1
    else:
        answer = number * factorial(number - 1)
    return answer

print(factorial(0))
print(factorial(5))  

