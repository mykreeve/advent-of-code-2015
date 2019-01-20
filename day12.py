import ast

filename="input/day12input.txt"
file=open(filename,"r")
file=file.readlines()
item=file[0]

item = ast.literal_eval(item)
output=[]
for k,v in item.items():
    output.append(k)
    output.append(v)
item=output

def contains_procs(item):
    for a in item:
        if type(a)==dict or type(a)==list:
            return True
    return False

while contains_procs(item):
    output=[]
    for ind in item:
        if type(ind)==dict:
            for k,v in ind.items():
                output.append(k)
                output.append(v)
        elif type(ind)==list:
            for v in ind:
                output.append(v)
        else:
            output.append(ind)
    item=output

total=0
for a in item:
    if type(a)==int:
        total += a

print ("Answer for part one: " + str(total))

item=file[0]

item = ast.literal_eval(item)
output=[]
for k,v in item.items():
    output.append(k)
    output.append(v)
item=output

def contains_red(dictObj):
    for k,v in dictObj.items():
        if v=='red':
            return True
    return False

while contains_procs(item):
    output=[]
    for ind in item:
        if type(ind)==dict:
            if contains_red(ind):
                pass
            else:
                for k,v in ind.items():
                    output.append(k)
                    output.append(v)
        elif type(ind)==list:
            for v in ind:
                output.append(v)
        else:
            output.append(ind)
    item=output

total=0
for a in item:
    if type(a)==int:
        total += a

print ("Answer for part two: " + str(total))