def path_exists(graph, start, target):
    visited = set()
    to_visit = [start]

    while to_visit:
        current = to_visit.pop()

        if current == target:
            return  True
        
        if current in visited:
            continue

        visited.add(current)

        for neighbour in graph[current]:
            to_visit.append(neighbour)
    return False

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(path_exists(graph,"A", "F"))
print(path_exists(graph, "D", "A"))




