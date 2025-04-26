def is_path_crossing(movements):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    for i, move in enumerate(movements):
        dx, dy = directions[i % 4]
        for _ in range(move):
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

    return False


print(is_path_crossing([0, 1, 2, 3]))
print(is_path_crossing([1, 2, 3, 4]))
print(is_path_crossing([2, 1, 1, 2]))
