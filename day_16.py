import copy

sample = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def walk(x, y, dir, grid,colors):
    step = 0
    directions = [(1, 0),  # 0 east
                  (0, 1),  # 1 south
                  (-1, 0),  # 2 west
                  (0, -1)]  # 3 north
    newdir = {"-": [0, -1, 2, -1],
              "|": [-1, 1, -1, 3],
              ".": [0, 1, 2, 3],
              "/": [3, 2, 1, 0],
              "\\": [1, 0, 3, 2]}

    done = False
    faker = None
    while not done:
        colors[y][x] = "x"
        step += 1

        if faker:
            c = faker
            faker = None
        else:
            c = grid[y][x]
        if c == ".":  # continue
            a, b = directions[dir]
            x += a
            y += b
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                break
            continue
        elif c == "/" or c == "\\":  # divert
            j = newdir[c][dir]
            if j == -1:
                raise AssertionError
            dir = j
            faker = "."
            continue
        elif c == "-":  # split
            if dir == 1 or dir == 3:
                grid[y][x] = "?"
                xa = x + directions[2][0]
                ya = y + directions[2][1]
                if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                    walk(xa, ya, 2, grid,colors)
                xa = x + directions[0][0]
                ya = y + directions[0][1]
                if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                    walk(xa, ya, 0, grid,colors)
            else:
                faker = "."  # skip next cycle
        elif c == "|":  # split
            if dir == 0 or dir == 2:
                grid[y][x] = "?"
                xa = x + directions[1][0]
                ya = y + directions[1][1]
                if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                    walk(xa, ya, 1, grid,colors)
                xa = x + directions[3][0]
                ya = y + directions[3][1]
                if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                    walk(xa, ya, 3, grid,colors)
            else:
                faker = "."  # skip next cycle
        else:
            done = True


with open("input16.txt", "r") as f:
    lines = f.readlines()
#lines = sample.splitlines()
initial_grid = list(map(lambda x: list(x.strip()), lines))
occupied = []
for i in list(map(lambda x: list(x.strip()), lines)):
    occupied.append(["_"] * len(initial_grid[0]))


def counting(x, y, direction):
    grid2 = list(map(lambda x: list(x.strip()), lines))
    empty_map = copy.deepcopy(occupied)
    walk(x, y, direction, grid2, empty_map)
    s = 0
    for i in empty_map:
        for j in i:
            if j == "x":
                s += 1
    #for i in empty_map:
    #    for j in i:
    #        print(j, end="")
    #    print("")
    return s


print("part A", counting(0, 0, 0))

print([counting(x,0,1) for x in range(len(initial_grid[0]))])
part_b = max([counting(x, 0, 1) for x in range(len(initial_grid[0]))])
print(part_b)
part_b = max([counting(x, len(initial_grid) - 1, 3) for x in range(len(initial_grid[0]))])
print(part_b)
part_b = max([counting(0,y,0) for y in range(len(initial_grid))])
print(part_b)
part_b = max([counting(len(initial_grid[0]) - 1, y, 2) for y in range(len(initial_grid))])
print(part_b)
