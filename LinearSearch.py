#Arrays are implemented using List
myList = []
#adding elements in an array
myList.append(67)
myList.append(45)
myList.append(78)
print(myList)
myList.pop(0)
print(myList)
my_New_List = [3,4,4,4,6,7,7,77,8,888,88,0]
print(my_New_List)
my_New_List.insert(5,78)
print(my_New_List)
my_New_List.remove(0)
print(my_New_List)
myList.clear()
print(myList)
print(len(myList))
print(my_New_List.count(4))

#Simple Linear Search
mylist = [5, 67, 7, 88, 9]

search = int(input("Enter number to search: "))

for i in range(len(mylist)):
    if mylist[i] == search:
        print("Found")
        break
else:
    print("Not found")
