def  first_position(numbers, target):
    low = 0
    high = len(numbers)-1

    result = -1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            result = mid

            high = mid -1
        elif numbers[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return result
print(first_position([2, 4, 4, 4, 8, 10],target = 4))
print(first_position([1, 3, 5, 7], target = 6))





    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
