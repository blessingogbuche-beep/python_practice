def closest_number(numbers, target):
    if not numbers:
        return None

    closest = numbers[0]
    for num in numbers:

        num_distance = abs(num - target)
        closest_number = abs(closest - target)
    
        if num_distance < closest_number:
            closest = num

        elif num_distance == closest_number and num < closest:
            closest = num

    return closest
print(closest_number([4, 8, 15, 20], target = 13))
print(closest_number([8, 12], target = 10))
