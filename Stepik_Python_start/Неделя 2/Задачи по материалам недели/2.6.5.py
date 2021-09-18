def massive(n):
    dx, dy = 1, 0
    x, y = 0, 0
    array = [[None] * n for _ in range(n)]
    for i in range(1, n ** 2 + 1):
        array[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not array[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    for x in list(zip(*array)):
        print(*x)


massive(int(input()))