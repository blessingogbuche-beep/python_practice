def find_numbers(numbers, target):
    for i in range(len(numbers)):
        
        if numbers [i] == target:
            return i
    return -1
print(find_numbers([10, 25, 30, 45], target = 30))
print(find_numbers([5, 8, 5, 9], target = 5))
print(find_numbers([10, 20, 30], target = 99))