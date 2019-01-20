filename="input/day16input.txt"
file=open(filename,"r")
file=file.readlines()

sues = {}
for item in file:
    item=item.strip().replace('Sue ','').replace(': ',',').replace(' ','').split(',')
    sues[int(item[0])]={item[1]:int(item[2]), item[3]:int(item[4]), item[5]: int(item[6])}

filename="input/day16knowns.txt"
file=open(filename,"r")
file=file.readlines()

knowns = {}
for item in file:
    item=item.strip().replace(': ',',').split(',')
    knowns[item[0]]=int(item[1])

for val in range(1, len(sues)+1):
    sue_eval=True
    for k,v in sues[val].items():
        if v!=knowns[k]:
            sue_eval=False
    if sue_eval:
        print ("Answer to part one: " + str(val))

for val in range(1, len(sues)+1):
    sue_eval=True
    for k,v in sues[val].items():
        if k in ['cats','trees']:
            if v<=knowns[k]:
                sue_eval=False
        elif k in ['pomeranians','goldfish']:
            if v>=knowns[k]:
                sue_eval=False
        else:
            if v!=knowns[k]:
                sue_eval=False
    if sue_eval:
        print ("Answer to part two: " + str(val))