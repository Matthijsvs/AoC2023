import copy

rules = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}"""

sample = """{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

d = {}
max_xms = {"x": (0, 99999), "m": (0, 99999), "a": (0, 99999), "s": (0, 99999)}
for i in rules.splitlines():
    name, rule = i.rstrip("}").split("{")
    d[name] = rule.split(",")

d["A"]="A"
d["R"]="R"
def split(workflow,inp):
    if workflow=="A":
        print("accepted",workflow,"-",inp)
        return [inp]
    res = []
    #print(workflow)
    for i in workflow:
        if ":" in i:
            cond, targ = i.split(":")
            name = cond[0]
            value = int(cond[2:])
            q = copy.deepcopy(inp)
            old = inp[name]
            if value > max(old) or value < min(old): #condition already met
                print(i, " outside!!! -->", q)
                res.extend(split(d[targ], inp))
            else:
                if cond[1] == "<":
                    q[name] = (min(old),value-1) #if true, new is smaller but start the same
                    inp[name] = (value,max(old)) # if false start at value until end
                else:
                    q[name] = (value+1,max(old)) #if true, new is bigger
                    inp[name] = (min(old),value)
                print(i,"-->",q)
                print("-->",inp)
                res.extend(split(d[targ], q))
        else:
            if i=="R":
                pass
            elif i=="A":
                res.extend([inp])
            elif i!="A":
                res.extend(split(d[i], q))
    return res
g = split(d["in"],max_xms)

print("-------------------")
for i in g:
    print(i)

for i in sample.splitlines():
    s = i.strip("{}").split(",")
    j = dict(map(lambda x: x.split("="), s))
    reject = True
    print(j)
    for itm in g:
        row = True
        for l in "xmas":
            if (int(j[l])<itm[l][0] or int(j[l])>itm[l][1]):
                row = False
        if row == True:
            reject=False
    print(reject)

