filename="input/day17input.txt"
file=open(filename,"r")
file=file.readlines()

containers=[]
for item in file:
    containers.append(int(item))

containers.sort()
print (containers)

solutions =[]

def add_sol(tup):
    tup = list(tup)
    tup.sort()
    if tup not in solutions:
        solutions.append(tup)
        print ("NEW SOLUTION FOUND: "+ str(tup) + " -- FOUND: " + str(len(solutions)))

for a in range(0, len(containers)):
    for b in range(1, len(containers)):
        if a==b:
            pass
        else:
            for c in range(2, len(containers)):
                if a==c or b==c or containers[a] + containers[b] + containers[c] > 150:
                    pass
                else:
                    if containers[a] + containers[b] + containers[c] == 150:
                        add_sol((containers[a], containers[b], containers[c]))
                    # print (a,b,c)
                    for d in range(3, len(containers)):
                        if a==d or b==d or c==d or containers[a] + containers[b] + containers[c] + containers[d] > 150:
                            pass
                        else:
                            if containers[a] + containers[b] + containers[c] + containers[d] == 150:
                                add_sol(( a,b,c,d ))
                            # print (a,b,c,d)
                            for e in range(4, len(containers)):
                                if a==e or b==e or c==e or d==e or containers[a] + containers[b] + containers[c] + containers[d] + containers[e] > 150:
                                    pass
                                else:
                                    if containers[a] + containers[b] + containers[c] + containers[d] + containers[e] == 150:
                                        add_sol(( a,b,c,d,e ))
                                    # print (a,b,c,d,e)
                                    for f in range(5, len(containers)):
                                        if a==f or b==f or c==f or d==f or e==f or containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f]> 150:
                                            pass
                                        else:
                                            if containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] == 150:
                                                add_sol(( a,b,c,d,e,f ))
                                            # print (a,b,c,d,e,f)
                                            for g in range(6, len(containers)):
                                                if a==g or b==g or c==g or d==g or e==g or f==g or containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] + containers[g] > 150:
                                                    pass
                                                else:
                                                    if containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] + containers[g] == 150:
                                                        add_sol(( a,b,c,d,e,f,g ))
                                                    # print (a,b,c,d,e,f,g)
                                                    for h in range(7, len(containers)):
                                                        if a==h or b==h or c==h or d==h or e==h or f==h or g==h or containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] + containers[g] + containers[h] > 150:
                                                            pass
                                                        else:
                                                            if containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] + containers[g] + containers[h] == 150:
                                                                add_sol(( a,b,c,d,e,f,g,h ))
                                                            # print (a,b,c,d,e,f,g,h)
                                                            for i in range(8, len(containers)):
                                                                if a==i or b==i or c==i or d==i or e==i or f==i or g==i or h==i or containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] + containers[g] + containers[h] + containers[i] > 150:
                                                                    pass
                                                                else:
                                                                    if containers[a] + containers[b] + containers[c] + containers[d] + containers[e] + containers[f] + containers[g] + containers[h] + containers[i] == 150:
                                                                        add_sol(( a,b,c,d,e,f,g,h,i ))
                                                                    # print (a,b,c,d,e,f,g,h,i)

print ("Answer to part one: " + str(len(solutions)))

min_length=999
for a in solutions:
    if len(a) < min_length:
        min_length = len(a)

short_solutions=0
for a in solutions:
    if len(a) == min_length:
        short_solutions += 1

print ("Answer to part two: " + str(short_solutions))