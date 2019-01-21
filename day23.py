filename="input/day23input.txt"
file=open(filename,"r")
file=file.readlines()

programme = []

for line in file:
    line = line.strip().replace(", ",",").replace(" ",",").replace("+","").split(',')
    if len(line)==3:
        programme.append((line[0],line[1],int(line[2])))
    elif line[0] == 'jmp':
        programme.append((line[0],int(line[1])))
    else:
        programme.append((line[0],line[1]))

def hlf(val):
    return int(val/2)

def tpl(val):
    return int(3*val)

def inc(val):
    return int(val+1)


a=0
b=0
position = 0
while position in range(len(programme)):
    command = programme[position]
    move=True
    if command[0] == 'hlf':
        if command[1] == 'a':
            a=hlf(a)
        if command[1] == 'b':
            b=hlf(b)
    if command[0] == 'tpl':
        if command[1] == 'a':
            a=tpl(a)
        if command[1] == 'b':
            b=tpl(b)
    if command[0] == 'inc':
        if command[1] == 'a':
            a=inc(a)
        if command[1] == 'b':
            b=inc(b)
    if command[0] == 'jmp':
        position += command[1]
        move=False
    if command[0] == 'jie':
        if command[1] == 'a' and a%2==0:
            position += command[2]
            move=False
        if command[1] == 'b' and b%2==0:
            position += command[2]
            move=False
    if command[0] == 'jio':
        if command[1] == 'a' and a==1:
            position += command[2]
            move=False
        if command[1] == 'b' and b==1:
            position += command[2]
            move=False
    if move:
        position += 1

print ("Answer for part one: " + str(b))


a=1
b=0
position = 0
while position in range(len(programme)):
    command = programme[position]
    move=True
    if command[0] == 'hlf':
        if command[1] == 'a':
            a=hlf(a)
        if command[1] == 'b':
            b=hlf(b)
    if command[0] == 'tpl':
        if command[1] == 'a':
            a=tpl(a)
        if command[1] == 'b':
            b=tpl(b)
    if command[0] == 'inc':
        if command[1] == 'a':
            a=inc(a)
        if command[1] == 'b':
            b=inc(b)
    if command[0] == 'jmp':
        position += command[1]
        move=False
    if command[0] == 'jie':
        if command[1] == 'a' and a%2==0:
            position += command[2]
            move=False
        if command[1] == 'b' and b%2==0:
            position += command[2]
            move=False
    if command[0] == 'jio':
        if command[1] == 'a' and a==1:
            position += command[2]
            move=False
        if command[1] == 'b' and b==1:
            position += command[2]
            move=False
    if move:
        position += 1

print ("Answer for part two: " + str(b))
