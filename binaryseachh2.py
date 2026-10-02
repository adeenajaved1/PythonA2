def binarySearch(numbers, target):
    low = 0
    high = len(numbers) - 1

    # Continue while at least one possible position remains
    while low <= high:

        # Find the middle index
        mid = (low + high) // 2

        # Case 1: Target found
        if numbers[mid] == target:
            return mid

        # Case 2: Middle value is smaller than target
        elif numbers[mid] < target:
            low = mid + 1

        # Case 3: Middle value is greater than target
        else:
            high = mid - 1

    # No possible position remains
    return -1


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

result = binarySearch(numbers, 70)

print(result)