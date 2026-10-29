def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(find_smallest([8, 3, 12, 1, 7])) 
print(find_smallest([-3, -10, -1, -6])) 




