import itertools

filename="input/day13input.txt"
file=open(filename,"r")
file=file.readlines()

happiness_scores={}
people=[]

for item in file:
    item=item.strip().replace(' would ',',').replace('lose ','-').replace('gain ','').replace(' happiness units by sitting next to ',',').replace('.','').split(',')
    happiness_scores[item[0],item[2]]=int(item[1])
    if item[0] not in people:
        people.append(item[0])

perms = list(itertools.permutations(people))

best_happiness=0
for table in perms:
    happiness=0
    for n,person in enumerate(table):
        if n<len(table)-1:
            happiness += happiness_scores[person,table[n+1]]
            happiness += happiness_scores[table[n+1],person]
        elif n==len(table)-1:
            happiness += happiness_scores[person,table[0]]
            happiness += happiness_scores[table[0],person]
    if happiness > best_happiness:
        best_happiness = happiness

print ("Answer for part one: " + str(best_happiness))

for n in people:
    happiness_scores['me',n] = 0
    happiness_scores[n,'me'] = 0
people.append('me')

perms = list(itertools.permutations(people))

best_happiness=0
for table in perms:
    happiness=0
    for n,person in enumerate(table):
        if n<len(table)-1:
            happiness += happiness_scores[person,table[n+1]]
            happiness += happiness_scores[table[n+1],person]
        elif n==len(table)-1:
            happiness += happiness_scores[person,table[0]]
            happiness += happiness_scores[table[0],person]
    if happiness > best_happiness:
        best_happiness = happiness

print ("Answer for part two: " + str(best_happiness))