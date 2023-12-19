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

sample ="""{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""



class workflow():
    def __init__(self,s):
        self.rules=[]
        g =s.split(",")
        for i in g:
            if ":" in i:
                cond, targ = i.split(":")
                if cond[1]=="<":
                    f = self.lt
                else:
                    f = self.gt
                self.rules.append((cond[0],f, int(cond[2:]), targ))
            else:
                self.rules.append((0,None,0,i))


    def process(self,line):
        for i in self.rules:
            letter,f,v,action = i
            print(f(line[letter],v))
            return True

    #@staticmethod
    def lt(self,a,b):
        print(a,"<",b)
        return a>b
    #@staticmethod
    def gt(self,a,b):
        return a<b
    #@staticmethod
    def accept(self,line):
        line["acc"]=True
        return

d = {}
for i in rules.splitlines():
    name,rule = i.rstrip("}").split("{")
    d[name]=workflow(rule)

src = []
for i in sample.splitlines():
    itm = i.strip("{}").split(",")
    x,m,a,s=[int(x[2:]) for x in itm]
    p = {"x":x,"m":m,"a":a,"s":s,"acc":False}
    d["px"].process(p)
    src.append(p)

#print(src)

