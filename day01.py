filename="input/day1input.txt"
file=open(filename,"r")
file=file.readlines()
file=file[0].strip()

floor=0
done=False
for n,m in enumerate(file):
    if m=='(':
        floor += 1
    elif m==')':
        floor -= 1
    if floor < 0 and done==False:
        done=True
        print ("Answer to part two: " + str(n+1))

print ("Answer to part one: " + str(floor))