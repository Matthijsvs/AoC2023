

def distance(maxtime, record):
    for time in range(maxtime):
        t = -1 * time**2 + maxtime*time
        yield t > record

def count(maxtime,record):
    count=0
    for i in distance(maxtime,record):
        if i:
            count+=1
    return(count)

a = count(59,597)
b = count(79,1234)
c = count(65,1032)
d = count(75,1328)
print(a*b*c*d)

a=count(59796575,597123410321328)
print(a)
