def insertionSort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1

        numbers[j + 1] = key

    return numbers


numbers = [7, 3, 8, 2, 6, 4, 5]

print(insertionSort(numbers))