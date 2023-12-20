import math
from dataclasses import dataclass
from threading import Condition

sample = """%jr -> mq, xn
%zl -> tz, cm
&lh -> nr
%hx -> jx, tz
%cm -> tz, ls
&fk -> nr
broadcaster -> sj, pf, kh, cn
%gz -> mq, lq
%gb -> xf, kr
%zc -> rq
%ln -> qj, xf
%gq -> pp
%fb -> xf
%pf -> tg, nv
%bc -> cf
&tz -> cn, fk, ls
%cq -> fb, xf
%rq -> tg, dx
%km -> gq
&mq -> gq, xn, fv, km, lh, xv, sj
%zp -> mq, xv
%jx -> tz, np
&tg -> mm, rp, zc, pf, bc
%cv -> sq, xf
%nv -> ht, tg
%sq -> gb
%kr -> ln
%dk -> cv
%xn -> zp
%sx -> xf, cq
%zt -> tz, fq
%dx -> tg, qn
&ff -> nr
%bn -> hx, tz
%fj -> zt, tz
%ht -> rr, tg
%fq -> tz, bn
%kh -> dk, xf
%sj -> mq, fv
%vm -> zl, tz
&mm -> nr
%rp -> bc
%fh -> sx
%ls -> fj
%xz -> mq, gz
%fv -> km
&nr -> rx
%lq -> mq
%xv -> xz
%cn -> tz, vm
%pp -> jr, mq
%hn -> tg
%qn -> hn, tg
%rr -> rp, tg
%cf -> tg, zc
%qj -> fh, xf
&xf -> sq, dk, fh, ff, kh, kr
%np -> tz"""

items = {}


@dataclass
class Pulse:
    frm: str
    to: str
    high: bool = False


class broadcaster():
    def __init__(self, outputs):
        o = outputs.split(",")
        self.o = [i.strip() for i in o]

    def getPulse(self, itm):
        res = []
        for i in self.o:
            res.append(Pulse(itm.to, i, itm.high))
        return res


class ConJunction(broadcaster):
    def __init__(self, outputs):
        super().__init__(outputs)
        self.state = True
        self.inputs = {}

    def addVal(self, inp):
        self.inputs[inp] = False

    def reset(self):
        self.inputs={}

    def getPulse(self, itm):
        res = []
        self.inputs[itm.frm] = itm.high
        # print(self.inputs.values())
        out = not all(self.inputs.values())
        self.state = out
        for i in self.o:
            res.append(Pulse(itm.to, i, out))
        return res


class FlipFlop(broadcaster):
    def __init__(self, outputs):
        super().__init__(outputs)
        self.state = False  # off

    def getPulse(self, itm):
        res = []
        if itm.high:  # ignore high pulse
            return res
        self.state = not self.state
        for i in self.o:
            res.append(Pulse(itm.to, i, self.state))
        return res


for i in sample.splitlines():
    inp, out = i.split("->")
    if inp == "broadcaster ":
        q = broadcaster(out)
        items[inp.strip("% &")] = q
    elif inp[0] == "%":
        q = FlipFlop(out)
        items[inp.strip("% &")] = q
    elif inp[0] == "&":
        q = ConJunction(out)
        items[inp.strip("% &")] = q

for i in items:
    for j in items[i].o:
        if j in items and isinstance(items[j],ConJunction):
            #pass
            items[j].addVal(i)

countH = countL = 0
for i in range(1000):
    q = [Pulse("Button", "broadcaster")]
    while q:
        next = q.pop(0)
        if next.high:
            countH += 1
        else:
            countL += 1
        # print(next)
        if next.to in items:
            q.extend(items[next.to].getPulse(next))
print(countL*countH)
steps = 0

bc_old = items["broadcaster"]
ans = {}
for j in bc_old.o:
    items["broadcaster"]=broadcaster(j)
    items["nr"].reset()
    steps=0
    for i in range(20000):
        q = [Pulse("Button", "broadcaster")]
        steps+=1
        while q and not j in ans:
            next = q.pop(0)

            if next.to in items:
                q.extend(items[next.to].getPulse(next))
            else:
                if next.high == False:
                    ans[j]=steps
                    break
        if j in ans:
            break

print(math.lcm(*ans.values()))