maps = """seeds: 
79 79 14 
55 55 13

map
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class Range():
    def __init__(self, s: str):
        out_range, in_range, length = [int(x) for x in s.split()]
        self.start = in_range
        self.end = in_range + length
        self.offset = out_range - in_range
        self.adjusted = (self.offset == 0)

    @classmethod
    def fromPair(cls, start, stop):
        return cls(f"{start} {start} {stop}")

    def translate(self):
        self.start += self.offset
        self.start += self.offset
        self.adjusted = True

    def split(self, pos):
        self.end = pos - 1

    def snoop(self, other):
        if other.start >= self.start and other.start <= self.end:
            print("overlap from start")
            return True
        elif other.end <= self.end and other.end >= self.start:
            print("overlap before end")
            return True
        elif other.start >= self.start and other.end <= self.end:
            print("overlap complete")
            return True
        elif other.start <= self.start and other.end >= self.end:
            print("overlap inside")
            return True

        print(self, other)
        return False

    def __lt__(self, other):
        return self.start < other.start

    def __repr__(self):
        if self.adjusted:
            return f"{self.start}-{self.end}"
        else:
            return f"{self.start}-{self.end} ({self.offset})"  # =>{self.start + self.offset}-{self.end + self.offset}"


# List for each map
levels = []
for m in maps.splitlines():
    if m and m[0].isdigit():  # continue the map
        levels[-1].append(Range(m))
    else:  # create new list for the map
        if m:
            levels.append([])

for j in levels:
    j.sort()

k = levels[0]
print(k)
left = k[0].start
right = k[1].end
next = [Range.fromPair(left, right)]
print(next)
