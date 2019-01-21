filename="input/day18input.txt"
file=open(filename,"r")
file=file.readlines()

grid={}

def setup_grid():
    global line
    for y, line in enumerate(file):
        line = line.strip()
        line = list(line)
        for x, char in enumerate(line):
            grid[x,y]=char

def neighbours_on(x,y):
    on=0
    if x>0 and y>0:
        if grid[x-1,y-1]=='#':
            on += 1
    if x>0:
        if grid[x-1,y]=='#':
            on += 1
    if x>0 and y<(len(line)-1):
        if grid[x-1,y+1]=='#':
            on += 1
    if y>0:
        if grid[x,y-1]=='#':
            on += 1
    if y<(len(line)-1):
        if grid[x,y+1]=='#':
            on += 1
    if x<(len(line)-1) and y>0:
        if grid[x+1,y-1]=='#':
            on += 1
    if x<(len(line)-1):
        if grid[x+1,y]=='#':
            on += 1
    if x<(len(line)-1) and y<(len(line)-1):
        if grid[x+1,y+1]=='#':
            on += 1
    return on

def count_on():
    on=0
    for y in range(len(line)):
        for x in range(len(line)):
            if grid[x,y]=='#':
                on += 1
    return on

def iterate_grid(grid):
    newGrid={}
    for y in range(len(line)):
        for x in range(len(line)):
            if grid[x,y]=='#' and (neighbours_on(x,y)==2 or neighbours_on(x,y)==3):
                newGrid[x,y]='#'
            elif grid[x,y]=='#':
                newGrid[x,y]='.'
            elif grid[x,y]=='.' and neighbours_on(x,y)==3:
                newGrid[x,y]='#'
            else:
                newGrid[x,y]='.'
    return newGrid

turn=0
setup_grid()

while turn<100:
    turn += 1
    grid=iterate_grid(grid)

print ("Answer for part one : " + str(count_on()))

turn=0
setup_grid()
grid[0,0]='#'
grid[0,len(line)-1]='#'
grid[len(line)-1,0]='#'
grid[len(line)-1,len(line)-1]='#'

while turn<100:
    turn += 1
    grid=iterate_grid(grid)
    grid[0,0]='#'
    grid[0,len(line)-1]='#'
    grid[len(line)-1,0]='#'
    grid[len(line)-1,len(line)-1]='#'

print ("Answer for part two : " + str(count_on()))
