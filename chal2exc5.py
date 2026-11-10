def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    for n in numbers:
        counts[n] = counts.get(n,0) + 1
        best = None
        best_count = 0

    for n in numbers:
        if counts[n] > best_count:
            best = n
            best_count = counts[n]

    return best
print(most_frequent([2, 5, 2, 8, 2, 5 ]))
print(most_frequent([4, 7, 7, 4]))
print([])
