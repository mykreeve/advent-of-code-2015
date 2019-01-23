import itertools
import functools
import operator

filename="input/day24input.txt"
file=open(filename,"r")
file=file.readlines()

packages = []

for line in file:
    packages.append(int(line))

target_weight = int(sum(packages)/3)

lowest_qe = 99999999999999999999999999999999999

for a in range(4,7):
    # print(str(a))
    comb = list(itertools.combinations(packages, a))
    # print(str(len(comb)))
    for i in comb:
        if (int(sum(i))) == target_weight:
            i = sorted(i)
            print (i)
            remains = [x for x in packages if x not in i]
            for c in range (4,12):
                # print (c)
                comb2 = list(itertools.combinations(remains, c))
                for b in comb2:
                    if (int(sum(b))) == target_weight:
                        qe = functools.reduce(operator.mul, i, 1)
                        if qe < lowest_qe and a==6:
                            lowest_qe = qe
                            first_group = i
                        break

target_weight = int(sum(packages)/4)

lowest_qe2 = 99999999999999999999999999999999999

for a in range(4,6):
    comb = list(itertools.combinations(packages, a))
    for i in comb:
        test = 0
        if (int(sum(i))) == target_weight:
            print (i)
            remains = [x for x in packages if x not in i]
            for c in range (4,12):
                # print (c)
                comb2 = list(itertools.combinations(remains, c))
                for b in comb2:
                    if (int(sum(b))) == target_weight:
                        new_remains = [x for x in remains if x not in b]
                        for d in range(4,12):
                            comb3 = list(itertools.combinations(new_remains, d))
                            for e in comb3:
                                if (int(sum(e))) == target_weight:
                                    qe = functools.reduce(operator.mul, i, 1)
                                    if qe < lowest_qe2 and a==5:
                                        lowest_qe2 = qe
                                        first_group2 = i
                                    test = 1
                                    break
                    if test == 1:
                        break
                if test == 1:
                        break


print ("Answer for part one: (" + str(first_group) + ") " + str(lowest_qe))
print ("Answer for part two: (" + str(first_group2) + ") " + str(lowest_qe2))





# def a_not_in_b(a,b):
#     for i in a:
#         for j in b:
#             if i==j:
#                 return False
#     return True

# def ab_not_in_c(a,b,c):
#     a = a+b
#     for i in a:
#         for j in c:
#             if i==j:
#                 return False
#     return True

# solutions = []

# for a in possibles:
#     print ("Assessing " + str(a) + " as first package")
#     more_possibles = []
#     for b in possibles:
#         if a_not_in_b(a,b):
#             more_possibles.append(b)
#     print ("There are " + str(len(more_possibles)) + " possible additionals")
#     for b in more_possibles:
#         for c in possibles:
#             if ab_not_in_c(a,b,c):
#                 print ("Found a solution: ", str(a), str(b), str(c))
#                 solutions.append((a,b,c))
    

