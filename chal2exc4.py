from collections import deque

def reversed_first(queue, k):
    stack = []

    for _ in range(k): 
        stack.append(queue.popleft())

    while stack:
            queue.append(stack.pop())


    for _ in range(len(queue) -k ):
            queue.append(queue.popleft())
               
q1 = deque([10, 20, 30, 40, 50])
reversed_first(q1, 3)
print(list(q1))

q2 = deque([1, 2, 3, 4, 5])
reversed_first(q2, 2)
print(list(q2))





