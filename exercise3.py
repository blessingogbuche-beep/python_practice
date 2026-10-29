def list_sum(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total

print(list_sum([2, 4, 6, 8]))
print(list_sum([-5, 10, -2]))
print(list_sum([]))


    

