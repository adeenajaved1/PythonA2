#code 1
names = ["Ali", "Sara", "Ahmed", "Ayesha"]

searchName = input("Enter name: ")

found = False

for i in range(len(names)):

    if names[i] == searchName:

        found = True

if found == True:

    print("Name found")

else:

    print("Name not found")


#code 2
numbers = [12, 7, 25, 4, 18]

total = 0

for i in range(len(numbers)):
    if numbers[i] > 10:
        total += numbers[i]

print("Total:", total)


#code 4
marks = [45, 67, 82, 39, 91, 55]

total = 0

for mark in marks:
    if mark >= 50:
        total += mark

print("Total of passing marks:", total)