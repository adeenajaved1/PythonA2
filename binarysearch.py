def binarySearch(numbers, target):

    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [0, 11, 44, 53, 77, 89, 99]

result = binarySearch(numbers, 110)

print(result)