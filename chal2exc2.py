def move_zeros(numbers):
    write = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[write] = numbers[i]
            write += 1

    for i in range(write, len(numbers)):
        numbers[i] = 0
a = [ 0,1,0,3,12]
move_zeros(a)
print (a)

b = [4, 0, 5, 0, 2] 

move_zeros(b)
print(b)

c = [1, 2, 3]
move_zeros(c)
print(c)
