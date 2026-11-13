def insertion_sort(numbers):
    shifts = 0

    for i in range(1, len(numbers)):

        current = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            shifts += 1
            j -= 1
            
            numbers[j + 1 ] = current
    return numbers, shifts

print(insertion_sort([5, 3, 4]))