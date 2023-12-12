sample = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def compare(t,s):
    print(f"[{t} = {s}]")
    p = True
    for i in range(len(s)):
        if s[i]=="." and t[i]=="#":
            return False
        elif s[i] == "#" and t[i] == ".":
            return False
    return p

def opts(s,groups):
    print("-----------------",s,groups)
    broken_springs = sum(groups)+len(groups)-1 #each broken spring is separated by 1 working
    working_springs = len(s) - broken_springs

    z=[]
    for i in range(working_springs+1):
        z.append(f"{i}")
    #print(z,len(z[0]))
    while len(z[0])<len(groups):
        q = []
        for i in range(working_springs + 1):
            for j in z:
                q.append(f"{i}{j}")
    print(z)
    t = ""
    for i in groups:
        t += "."*x
        t += "#"*i
        t +="."
    print(compare(t,s))

sum_a=0
for i in sample.splitlines():
    a,b = i.split()
    groups=[int(x) for x in b.split(",")]
    opts(a,groups)
print(sum_a)