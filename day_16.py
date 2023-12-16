from PIL import Image, ImageDraw
sample = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""


grid = []
colors = []

def bslash(x,y,im):
    shape = [(x*4, y*4), ((x+1)*4, (y+1)*4)]
    im.line(shape, fill ="black", width = 0)
def slash(x,y,im):
    shape = [((x+1)*4, y*4), (x*4, (y+1)*4)]
    im.line(shape, fill ="black", width = 0)

def beam2(x, y, dir,im):
    steps=0
    while 0 <= x < len(grid[0]) and 0 <= y < len(grid) and steps<100:  # loop until we're back
        steps += 1
        c = grid[y][x]
        colors[y][x] = "x"

        directions = [(1, 0),  # 0 east
                      (0, 1),  # 1 south
                      (-1, 0),  # 2 west
                      (0, -1)]  # 3 north

        u, v = directions[dir]
        shape = [(x*4+2,y*4+2),(x*4+2+-2*u,y*4+2+-2*v)]
        #im.rectangle((x*4, y*4, (x+1)*4, (y+1)*4), outline=(0, 0, 255))
        im.line(shape, fill="red", width=0)

        newdir = {"-":[0,-1,2,-1],
                  "|":[-1,1,-1,3],
                  ".":[0,1,2,3],
                  "/": [3, 2, 1, 0],
                  "\\": [1, 0, 3, 2]}


        if ((dir == 1) or (dir == 3)) and (c == "-"):
            shape = [(x * 4 , y * 4 + 2), (x * 4 + 4 , y * 4 + 2)]
            im.line(shape, fill="black", width=0)
            grid[y][x] = "?"
            xa = x + directions[0][0]
            ya = y + directions[0][1]
            if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                beam2(xa, ya, 0,im)

            xa = x + directions[2][0]
            ya = y + directions[2][1]
            if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                beam2(xa, ya, 2,im)
            break
        elif ((dir == 0) or (dir == 2)) and (c == "|"):
            grid[y][x] = "?"
            shape = [(x * 4 +2, y * 4 ), (x * 4 +2, y * 4 + 4)]
            im.line(shape, fill="black", width=0)
            xa = x + directions[1][0]
            ya = y + directions[1][1]
            if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                beam2(xa, ya, 1, im)
            xa = x + directions[3][0]
            ya = y + directions[3][1]
            if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                beam2(xa, ya, 3,im)
            break
        elif c in newdir:
            next_step = newdir[c][dir]
            if next_step == -1:
                raise AssertionError
            xa = x + directions[next_step][0]
            ya = y + directions[next_step][1]

            if 0 <= xa < len(grid[0]) and 0 <= ya < len(grid):
                u, v = directions[next_step]
                shape = [(x * 4 + 2, y * 4 + 2), (x * 4 + 2 + (2 * u), y * 4 + 2 + (2 * v))]
                im.line(shape, fill="green", width=0)
                dir = next_step
                x = xa
                y = ya
                if grid[y][x]=="?":
                    break
            else:
                print("Outside!")
                break
        elif c == "?":
            print("end found??")
            break
        else:
            #print(f"else situation {x},{y} --> {xa},{ya}",c,dir)

            break
            raise IOError("got lost along the way")
    #print("out of while loop",xa,ya,c,dir)

with open("input16.txt","r") as f:
    # for y in sample.splitlines():
    for y in f.readlines():
        grid.append(list(y.strip()))
        colors.append([" "] * len(grid[0]))

with Image.new("RGBA", (len(grid[0]*4), len(grid)*4), (255, 255, 255, 255)) as im:
    imageSizeW, imageSizeH = im.size
    img1 = ImageDraw.Draw(im)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == "/":
                slash(x,y,img1)
            elif grid[y][x] == "\\":
                bslash(x,y,img1)
    beam2(0, 0, 0,img1)  # top, left, east
    # for x in range(len(grid[0])):
    #    for y in range(len(grid)):
    #        if colors[j][i] == "x":
    #            im.putpixel((i, j), (255, 0, 0, 255))

im.save("day16.png", "PNG")

for i in grid:
    for j in i:
        print(j,end="")
    print("")
sum_a=0
for i in colors:
    sum_a+=i.count("x")
    for j in i:
        print(j,end="")
    print("")
print(sum_a)