def move_zeros(numbers):
    result = []
    zero_count = 0
    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)
    for _ in range(zero_count):
        result.append(0)
        return result
print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))