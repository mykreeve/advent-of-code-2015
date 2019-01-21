import copy

target_molecule='CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
reactions=[]

filename="input/day19input.txt"
file=open(filename,"r")
file=file.readlines()

for line in file:
    line=line.strip().replace(' => ',',').split(',')
    reactions.append((line[0],line[1]))

def find_str(s, char):
    finds = []
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    finds.append(index)
            index += 1
    return finds

resulting = []

for reaction in reactions:
    if reaction[0] in target_molecule:
        react_len=len(reaction[0])
        locs = (find_str(target_molecule, reaction[0]))
        for loc in locs:
            test_molecule = target_molecule[:loc] + reaction[1] + target_molecule[(loc+react_len):]
            if test_molecule not in resulting:
                resulting.append(test_molecule)

print ("Answer to part one: " + str(len(resulting)))


queue = [(0,target_molecule)]
visited = []
best = {}

molecule = copy.deepcopy(target_molecule)
count = 0
shuffles = 0
while len(molecule) > 1:
    start = molecule
    for frm, to in reactions:
        while to in molecule:
            count += molecule.count(to)
            molecule = molecule.replace(to, frm)

    if start == molecule:
        shuffle(reactions)
        molecule = copy.deepcopy(target_molecule)
        count = 0
        shuffles += 1

print ("Answer to part two: " + str(count))