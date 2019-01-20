import math
filename="input/day14input.txt"
file=open(filename,"r")
file=file.readlines()

after=2503
reindeer=[]
distance=[]

for item in file:
    item=item.strip().replace(' can fly ',',').replace(' km/s for ',',').replace(' seconds, but then must rest for ',',').replace(' seconds.','').split(',')
    reindeer.append(( item[0], int(item[1]), int(item[2]), int(item[3]) ))

for deer in reindeer:
    reps=math.floor(after/(deer[2]+deer[3]))
    dist=reps*(deer[1]*deer[2])
    remaining=after-(reps*(deer[2]+deer[3]))
    if remaining>deer[2]:
        remaining=deer[2]
    dist=dist+remaining*deer[1]
    distance.append((deer[0],dist))

best=0
for d in distance:
    if d[1]>best:
        best_deer = d[0]
        best=d[1]

print ("Answer for part one: " + best_deer + " went " + str(best))

besties={}

for sec in range(1,after+1):
    distance=[]
    for deer in reindeer:
        reps=math.floor(sec/(deer[2]+deer[3]))
        dist=reps*(deer[1]*deer[2])
        remaining=sec-(reps*(deer[2]+deer[3]))
        if remaining>deer[2]:
            remaining=deer[2]
        dist += remaining*deer[1]
        distance.append((deer[0],dist))

    best=0
    for d in distance:
        if d[1]>best:
            best=d[1]

    for d in distance:
        if d[1]==best:
            if d[0] not in besties:
                besties[d[0]]=1
            else:
                besties[d[0]] += 1

best=0
for k,v in besties.items():
    if v>best:
        best_deer = k
        best=v

print ("Answer for part two: " + best_deer + " scored " + str(best))
