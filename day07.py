filename="input/day7input.txt"
file=open(filename,"r")
file=file.readlines()

values={}
comm_done=[]
converted=[]
for line in file:
    line=line.strip().replace(' -> ',',=,').replace(' ',',').split(',')
    converted.append(line)

def to_binary16bit(dec):
    temp=str(bin(dec)[2:])
    while len(temp)<16:
        temp='0'+temp
    return temp

def from_binary16bit(bin):
    return (int(bin, 2))

def do_minor(action, val):
    if action=='NOT':
        temp=list(to_binary16bit(val))
        temp2=''
        for c in temp:
            if c=='0':
                temp2=temp2+'1'
            else:
                temp2=temp2+'0'
        return from_binary16bit(temp2)

# Yes, I made very heavy weather of this puzzle.
# I didn't trust Python to do 16-bit binary operations, so 
# wrote my own code to convert to binary and do the things.
# This was entirely unnecessary. D'oh.
def do_action(first, action, second):
    if action=='AND':
        first=list(to_binary16bit(first))
        second=list(to_binary16bit(second))
        res=''
        for n,c in enumerate(first):
            if first[n]=='1' and second[n]=='1':
                res = res + '1'
            else:
                res = res + '0'
        return from_binary16bit(res)
    elif action=='OR':
        first=list(to_binary16bit(first))
        second=list(to_binary16bit(second))
        res=''
        for n,c in enumerate(first):
            if first[n]=='1' or second[n]=='1':
                res = res + '1'
            else:
                res = res + '0'
        return from_binary16bit(res)
    elif action=='LSHIFT':
        first=list(to_binary16bit(first))
        res=''
        for n in range(len(first)):
            k = n+second
            if k>(len(first)-1):
                res = res + '0'
            else:
                res = res + first[k]
        return from_binary16bit(res)
    elif action=='RSHIFT':
        first=list(to_binary16bit(first))
        res=''
        for n in range(len(first)):
            k = n-second
            if k < 0:
                res = res + '0'
            else:
                res = res + first[k]
        return from_binary16bit(res)

def do_calc():
    while 'a' not in values:
        for n,command in enumerate(converted):
            if n not in comm_done:
                first=None
                second=None
                action=None
                # X = Z
                if command[1]=='=':
                    if command[0].isdigit() and command[2] not in values:
                        values[command[2]]=int(command[0])
                        comm_done.append(n)
                        # print (command[2] + " = " + command[0])
                    if command[0] in values:
                        values[command[2]]=values[command[0]]
                        comm_done.append(n)
                        # print (command[2] + " = " + command[0])
                # ACTION X = Z
                if len(command)>2 and command[2]=='=':
                    action=command[0]
                    if command[1] in values:
                        second=values[command[1]]
                    if (action and second) or (action and second==0):
                        values[command[3]]=do_minor(action,second)
                        comm_done.append(n)
                        # print(command[3] + " = NOT " + command[1])
                # X ACTION Y = Z
                if len(command)>3 and command[3]=='=':
                    if command[0].isdigit():
                        first=int(command[0])
                    elif command[0] in values:
                        first=values[command[0]]
                    if command[2].isdigit():
                        second=int(command[2])
                    elif command[2] in values:
                        second=values[command[2]]
                    action=command[1]
                    if (first and second and action) or (first==0 and second and action) or (first and second==0 and action) or (first==0 and second==0 and action):
                        values[command[4]]=do_action(first,action,second)
                        comm_done.append(n)
                        # print (command[4] + " = " + command[0] + " " + command[1] + " " + command[2])

do_calc()
print ("Answer to part one: " + str(values['a']))

values={ 'b': values['a'] }
comm_done=[]
do_calc()

print ("Answer to part two: " + str(values['a']))