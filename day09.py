import itertools

filename="input/day9input.txt"
file=open(filename,"r")
file=file.readlines()

distances={}
cities=[]

for line in file:
    line = line.replace(' to ', ',').replace(' = ', ',')
    line = line.strip().split(',')
    a,b,dist = line
    distances[a,b]=int(dist)
    distances[b,a]=int(dist)
    if a not in cities:
        cities.append(a)
    if b not in cities:
        cities.append(b)

perms = list(itertools.permutations(cities))

shortest = 9999
longest = 0

for option in perms:
    distance=0
    for i in range(len(option)-1):
        distance += distances[option[i],option[i+1]]
    if distance < shortest:
        shortest = distance
    if distance > longest:
        longest = distance

print ("Answer to part one: ", shortest)
print ("Answer to part two: ", longest)
