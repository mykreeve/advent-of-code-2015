filename="input/day6input.txt"
file=open(filename,"r")
file=file.readlines()

grid={}

def act(action,x,y):
    if action=='on':
        grid[x,y]=1
    elif action=='off':
        grid[x,y]=0
    elif action=='toggle':
        if (x,y) not in grid:
            grid[x,y]=1
        else:
            if grid[x,y]==0:
                grid[x,y]=1
            elif grid[x,y]==1:
                grid[x,y]=0
    elif action=='on2':
        if (x,y) not in grid:
            grid[x,y]=1
        else:
            grid[x,y] += 1
    elif action=='off2':
        if (x,y) not in grid:
            grid[x,y]=0
        else:
            grid[x,y] -= 1
            if grid[x,y] < 0:
                grid[x,y]=0
    elif action=='toggle2':
        if (x,y) not in grid:
            grid[x,y]=2
        else:
            grid[x,y] += 2

def do_func(action,minX,minY,maxX,maxY):
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            act(action,x,y)

for line in file:
    line=line.strip().replace("turn on ", "on,").replace("turn off ", "off,").replace("toggle ", "toggle,").replace(" through ", ",").split(",")
    # print (line)
    do_func(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]))

lights_on=0
for x in range(1000):
    for y in range(1000):
        if (x,y) in grid and grid[x,y]==1:
            lights_on += 1

print("Answer to part one: " + str(lights_on))

grid={}

for line in file:
    line=line.strip().replace("turn on ", "on2,").replace("turn off ", "off2,").replace("toggle ", "toggle2,").replace(" through ", ",").split(",")
    # print (line)
    do_func(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]))

lights_pow=0
for x in range(1000):
    for y in range(1000):
        if (x,y) in grid:
            lights_pow += grid[x,y]

print("Answer to part two: " + str(lights_pow))
    