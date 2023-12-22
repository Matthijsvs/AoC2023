import copy
from dataclasses import dataclass

sample = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##...####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
inp = """...................................................................................................................................
.....###.........#..#.........#.............#........##....#................##.......#..#.#.....#......#..#..#..##........#........
.#.............#............#...#.#...#.............#....#.................#.......#................#.....#....#.................#.
..#.......#..........#..........#......#.........#........................#.#...##.........#.......#.....#.##..#.............#.....
....#...#..##......#................##......#..#..#........................##.......#.............#..............##................
........#....#........#..#......#....#......#........#.........................#.....#.#.........#.................#..#..##....#...
.......................#...#.....#.....#..........#..#.........#............##.#...........#.....#..#.##..........#......#.#.....#.
..........#..........#....#.##.#...................#..#...........#...............#...........................#.....#.......##.....
.#.##..........#....#.#...#.....#.............#...............#.....................#.......#.#......#..................#..#.......
......#.#.#...................#..#.............................#...............#....#..............................###...........#.
....#...#...................#..................#...........####....#...............#....#..#.................#................#....
.............#..#.#..##.....#...#.......##.#...............#.........##..........#......................##....##....#.......#...#..
....#....#......###.#......#..#....#..#.........#....................................................#............#.........#.#....
.......#.#........##........#..#............#.##.............#..#...#....................#.#.....##.................#..............
....#....#....##...#..#......#.#.......................##......#.......................#..#.#..........#.#...........#..........#..
.#.......#..#......#......#..#............................##..........................#.............#.......#...##.#...............
...#..#...................#....#....#.....##...........#...............#...#...........#.#.#..#.#.#.#.#..#..#...#.#....#...........
.....................#..#.#..#..#..........#........#.................#.......#.......#.#......#.#..#........#............##.......
.......................................#...#.................###...##.#.....##.........##.........#..............#........#........
........#.##.........#........#.....##.............#...#...............#...................#..#.................#.........#.....#..
..#..#.#........#.....#.................................#............#.#....#.#...............##...#.....#............#..#.........
....#......#.....#....................#.........#.................#......................................................#.#....#..
....##...#...##..........#..............................#..#...#....#.......................#.#.#.....#.......#..#............##...
.#.....#.........#........#...#.....###...........#...............#.#...........#.#..........##..#..#................#..........#..
...#..#.#.#.......................................................#.##...#..........##............#..#.....#.........###...#....#..
......###.......#.#....##......#..#....................#........#.............#.#..........................#....#......###..#....#.
........#..........#......#....#.............#..#.................#..............................#.......#.#................#......
.#........#...........#.........#.....................#.........#........##.#.###......................####..#.#....#............#.
..##........#............#.#.......................#.....#.##.................#..#....#............................................
.............#..##....#.#.#...............#..................#.......##.#.....#...................##...##...#.##.............###...
......#..#....##.............................#.............................#..#....#....##.........#...#................#...#.##.#.
..#...........#........................#...........#....#...............#...............#...................#......................
....#...#.#.#...........#.#................###...............#.....##........#........................#.....##...#.#..........#....
.#..#.............#...#....##........#...#.............#............................#..#..#...........#...............##...........
...#......#..........................#.#.....##........#...#.......#...#...........##......#..............#..#.#...#.....#.#....#..
.#.#..............#................##.....#........#.....##...#....................#......#..#..............................#......
.#....................#.............#....#.............##.......#...........#.#......#...................##...#..............#.....
.....#.#...#.........##................#......#.....#...#....##.....................................................##.............
.............#........#............#.#.....#.........##.................##.....###.........#...............#....#..........#.....#.
..#.#...#....#...#......................##............#...#.#..#.........##.................................#......#........#....#.
..#.....#..................................#.#.....................#..#....#.....###..#.#...#..#.....#.......#..#..................
....#....##.#.....#.......................#.#...#......#.......................#.....#.........#....#...............#.......#......
....#.###.#......#...................#.............#...............##.........##........#......#....#..........#........##....###..
.....###....#...#.......................##.#....#.#...#.#..........#...#.....#......#.........#........#............#.....#...#....
...#.#.....#..#..............................##....#......#....#............#..#.#............#...#................................
...............#........##.#####.#......#.........................#....................#.#.#...##.#.##.#.#..................##.....
..#............................#.............#.#....#..........##.......#.#......#.#.#........#..#.#.##..................#.........
..##..##.#.............#..#.....#..#....#.#.#......#........#.................##.............#......#....#.#...........#......#..#.
..........##.#.........#.....##...................#.#...#...........................#........#...........................####......
.#......#.#.#.......#...............#.##..........#........#.................#..#.#.......#.............#....#.....................
.#.....#..#........#..#.....#...........#.#.....#.#.#...#..#..#.....#..........#.#......#............###.#.#...............#.....#.
..................##...#.......#...............#...........#.......#...............#........................................#......
.##.................#..#........#......##.............#..#.#..#....................#....................##.#.............###.......
.#......#...........#..........#...................#.........#.......##...........##..#......#.#....#.....#........................
.........................#.#.....#..#....#...#......#......................#............#................#.........................
....#....................#...#..#..............#..#...#..#..#...............#.....................#...........#..##...........#....
....#.........#...........#.....................#.#....#...#.................##.......#.#.........#...#............##..............
......................#........#...#...................#...#.###....#....#....#...............#....#...#....#......................
..................##......................##.....#...........#..........##..##.#......##............#.##...........................
.#.....................#.......#.................#..#........#...........#.#....#......#........#...........#......................
...........#.........#....#..#.#.#....#..#.......##.........#.............................#....#..#......#.#...#........#..........
.........#.........#.#....#.#.......................#..#......................#.................#....................#.#.#.........
......................#...#...#.........##.....#..............##......#...###......#...#....#.....##...........##........##........
............##..#.#......#...#.............#..#..#.........#...........#...#..#.........#...#......................................
...........#...........#..#......##..........#........#....#....#........#..................#...#.......##..#..#..#......#.........
...................................................................................................................................
..............#...#......#..#.....#................##......#............#........#........#..............#......#...........#......
...........#..#......#..#....#.....#..................#.....#...............#....#.....#..........#............#.#......#..#.......
..............#........#.#....#...#............#....#......#..........................................#.............#....#.........
..................#...#...............#.#...#..........#......................#.#.#.#.......#.....#..#........###..................
...................#.........##.#.#.....#..........#...........#.........#.#..#..##......#........#................................
.#.................#.....#.....#.##........#..........#...........#....#.....#...#.....#.........#..#........#.......#.#...........
..................#........#......##.#....##...#.#....#..#.....#....#...................#.....#...##...#.#......................#..
...##..............#..................#......................#.........##...#....#..#....#...........#.#..#........#...........#...
..#..#.............#................#............#............#.......#..#...##.....#.......#.......#.....#..................#.#...
..#.............#...................................#.............#......................................#..........#..............
.....#................#......#..#............#......#..#.##.#......#.......#.....#..#.........................##...........#...#.#.
...#.#............#......##........#.............#.....#..............#......###......#................#..................#......#.
....#...#.........#..#.##...###.#..............#........#..............#.#.........##....#.#.#......#....#.................#...#...
.##...#..#..........##............#........###.....#............#..#.........#............#.#.#........#..#..###............#......
.......#.................#.......#...#.......#..#......#..............#......#..##.................##....#.......................#.
...........................#.....#........#..#..............#.....##..........#....#..............#..#......##.............#.......
......#.................#................#...#.......................#.#.......##..#.........#....#.....##.............#.#.....#...
........................#.#.#.....##.......##.#........##.....#.....#...#....................#..........#..........................
.#...#........#............#.....#...#.....................#...........#.............#.##.#.....#......#.#...................#...#.
.....#..........#...........#...........................#.#.........#.............#..#.#..#...#.#....#..##..........#...........#..
.....#....#..#..................#....#...#......................#.......#..................#.......................#....#....#..#..
...#..............#...........#.#...........#.........#....#.........#.##.#..#......##.........#...##............##..#.#..#.....#..
..#............................#...#.....#......#.........#...#.....................#.....#.....#..#..#.............#..#...........
......#....#.....#.....................#.#.......#.#.#.....##.......#...#.............#..#.......#.............#..........#.#......
...............##..#................#.........#...##......#..#......#.#..#..........###..#..#..##............#..........#...#....#.
.#....#...........#..#.........#.#.#....#....#.........#.#............#....#...............##..................#.....#......#......
........#...#.....#.#................#...#....#..#....#.#..#.........#...#.................#..#.........................#..........
.........##...........................................#.................#...#.....#..#...##......#.........##............#...#.....
..#..#..#...#.#..................#....#.................#.#...#.........#.......#......##..#....#.........#......#....#............
...#...#......#....##...................##....#......#......#......#.......#.................#..#.............#.#..................
.#...#...#..##......#.#................#.#.................##..##.#..#...#.........#.........#..........................#..##......
.....................#..#..............#.......#..#...##.....................##...#....#.......................#..........#........
.......#.........#.#.....##..........#..#......#......#..#......#...#..................#....#......................................
.....#...#.....#........##......................##..................#..#...#.........###.#..#............................#.#....#..
........#....#...........#..#..........#.#.........................................#..#....#.......#...#...#...............###.....
....##..............#..#.................#..........#...........#.....#.....#....#....#.##....................#......#..#..........
..#..#..##..........##....#.#....................#.....#.#.....#............#.#........#............#....................#......#..
..........#..##......##........#....................#..#.#.............#......#........#.........#.....#....##..............##..#..
.#.......#...........#.......#.............#......###.....##.#....#....#..#....#...............................#.#..#...#.#....#...
............#....##...........#.............#.......................#......#.#...#...............##...#.....#...................#..
..#........#.........#....#..........................#....................###................#....................#.#..............
.....#..#.#........#............#.#..##.......#.....#..#...........#.........................#.......#.....#.......#........#...#..
.....##........................#..#.............#..............##.....#.....#.....#........#................#....#..##.#.........#.
..#...#........#.#...........#...#..............#.#.....#.....#.......................................#..#.#..................#....
...........#.#.....#..........#.#.......#.................#.......#.#...........#.............##........#.............#...#..#.#...
....#.....#....##.#........##..#..#.#........................#.........#.......#.........#.....###.....#.#.........................
.......#.....#.........#....#..#....#.....#..........#.#.#.........#.....#....#.........#.................#..........#...#.........
.#......#.........#..#...#......#.............................#...........#...............#.......#...#..........#...#......###....
.....................#..............#.#......#...........#......#....#.#...##.............#...##.#..#.###.#..............#.........
.#...#.............#.....#.....##..#........#............#..##....###....#.................#..#.#...##.#...#..........#...#.#......
.........#..#.....#..........................#.#..........##..#...##......................#...................#.....#............#.
.....#...##............#.........##...###......#...................#..................................#...........##..#............
.......#......................#....#...#..................#........#.#...#...........#.................#........#..........#.#.....
............#..............#.#.#..........#...#............#.......#............#.#.....#..##....#...#.#.....##........#...........
...........##.#..#...........#...#.....#.....#.............#......................#...........#...#.#.....#.......#..#..#..........
...#.#......#..#..#...............................#.............#.#..................#....#.#....#..............#................#.
.....#..................#...##.....#.#..#.#.#...................#..........................#.................#....#.....#..........
.............#..#..#....#.#..#..##...............#...............................#....#........#..#..#.......##.#........#.........
....#....#................##..#.........#.#..#....................#..............#...#......#...#..#...............................
......#....##.........##..............#....#....#.#..#..#....................................#...........#.#.#.#.###......#........
.#.#.....#.#..#.....#.....#.......##...#.......................................##......................#..........#.#....#..##..#..
............#..#.#........#..........#....#..#.....#.....#................#....##...........#...##....##.##....##.....##.#.........
...#....#...##..#.#.........#............#.........#.......................##..#.............................##....#..#.........#..
.......#.#............#...#...##....##.#..##..............#............#..............#....#.....#...#....##....#....#........#....
..................................................................................................................................."""
N = (0, -1)
NE = (1, -1)
E = (1, 0)
SE = (1, 1)
S = (0, 1)
SW = (-1, 1)
W = (-1, 0)
NW = (-1, -1)
STAY = (0, 0)
moves = [N, E, S, W]


@dataclass
class Point:
    x: int
    y: int
    steps: int = 0

    def __hash__(self):
        return self.x * 1000 + self.y


def get_next(p: Point):
    res = []
    for move in range(len(moves)):
        x = p.x + moves[move][0]
        y = p.y + moves[move][1]
        if grid[y % h][x % w] == ".":
            res.append(Point(x, y, p.steps + 1))
    return res

def ctr():
    yy = copy.deepcopy(grid)
    s = 0
    for p in plist:
        if 0 <= p.y < h and 0 <= p.x < w:
            yy[p.y][p.x] = "O"
    for j in yy:
        s += j.count("O")
        print("".join(j))
    print("----")
    return s

grid = []
b = 0
for y in inp.splitlines():
    grid.append(list(y))
    b+=y.count("#")

w = len(grid[0])  # highest width
h = len(grid)

start = Point(w // 2, h // 2)
steps = 130
plist = [start]
done=[]
res={}
for i in range(steps):
    n = []
    for j in plist:
        if j not in done:
            n.extend(get_next(j))

    plist = list(set(n))
    if i in [63,64,128,129]: #64, 65 and 130 steps
        res[i]=ctr();

print(res)
print("part A:",res[63])
num_fields = (26501365 - 65) // 131
total_fields = (1+2*num_fields)**2
outsides =  total_fields // 2
diamonds = outsides + 1
print(outsides,diamonds)
print("part B:",diamonds*res[64]+outsides*(res[128]-res[64]))
