filename="input/day3input.txt"
file=open(filename,"r")
file=file.readlines()
file=file[0].strip()

presents={(0,0): 1}
loc=(0,0)
for n in file:
    x,y=loc
    if n=='^':
        y=y-1
    if n=='>':
        x=x+1
    if n=='v':
        y=y+1
    if n=='<':
        x=x-1
    if (x,y) not in presents:
        presents[x,y]=1
    else:
        presents[x,y] += 1
    loc=(x,y)

presented=0
for k,v in presents.items():
    if v>=1:
        presented += 1

print ("Answer to part one: " + str(presented))

file=list(file)
presents={(0,0): 1}
loc=(0,0)
roboLoc=(0,0)
for no,n in enumerate(file):
    if no%2!=0:
        x,y=loc
        if n=='^':
            y=y-1
        if n=='>':
            x=x+1
        if n=='v':
            y=y+1
        if n=='<':
            x=x-1
        if (x,y) not in presents:
            presents[x,y]=1
        else:
            presents[x,y] += 1
        loc=(x,y)
    else:
        x,y=roboLoc
        if n=='^':
            y=y-1
        if n=='>':
            x=x+1
        if n=='v':
            y=y+1
        if n=='<':
            x=x-1
        if (x,y) not in presents:
            presents[x,y]=1
        else:
            presents[x,y] += 1
        roboLoc=(x,y)

   
presented=0
for k,v in presents.items():
    if v>=1:
        presented += 1

print ("Answer to part two: " + str(presented))