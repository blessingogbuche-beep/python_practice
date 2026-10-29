def count_occurences(numbers, target):
    count = 0
    for value  in numbers:
        if value == target:
            count += 1
    return count
print(count_occurences([2, 5, 2, 8, 2], target = 2))
print(count_occurences([1, 4, 7], target = 10))




