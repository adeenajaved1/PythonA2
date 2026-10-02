# List = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# SearchItem = 70

# MaxItems = len(List)

# Found = False
# SearchFailed = False

# First = 0
# Last = MaxItems - 1

# while not Found and not SearchFailed:

#     Middle = (First + Last) // 2

#     if List[Middle] == SearchItem:
#         Found = True

#     else:
#         if First >= Last:
#             SearchFailed = True

#         else:
#             if List[Middle] > SearchItem:
#                 Last = Middle - 1
#             else:
#                 First = Middle + 1


# if Found == True:
#     print(Middle)
# else:
#     print("Item not present in array")
# DataStored = [10, 20, 30, 40, 50, 60, 70]
# NumberItems = len(DataStored)


# def BinarySearch(DataToFind):
#     global DataStored
#     global NumberItems

#     First = 0
#     Last = NumberItems - 1

#     while First <= Last:
#         MidValue = int((First + Last) / 2)

#         if DataToFind == DataStored[MidValue]:
#             return MidValue

#         if DataToFind < DataStored[MidValue]:
#             Last = MidValue - 1
#         else:
#             First = MidValue + 1

#     return -1


