value = list("cqjxjnds")

alpha = list("abcdefghijklmnopqrstuvwxyz")

def iterate(value):
    position = len(value)-1
    while value[position]=='z':
        position -= 1
    for a in range(len(alpha)):
        if alpha[a] == value[position]:
            nextVal = a+1
    value[position] = alpha[nextVal]
    if position < len(value)-1:
        for a in range(position+1, len(value)):
            value[a] = 'a'
    return value

def password_contains_charas(value):
    if 'i' in value or 'o' in value or 'l' in value:
        return True
    else:
        return False

def password_doesnt_contain_triple(value):
    for a in range(0,len(value)-2):
        for b in range(len(alpha)):
            if alpha[b] == value[a]:
                charaPos = b
        if charaPos <= 23 and value[a+1]==alpha[charaPos+1] and value[a+2]==alpha[charaPos+2]:
            return False
    return True

def password_doesnt_have_two_pairs(value):
    pairs=[]
    for a in range(0,len(value)-1):
        if value[a]==value[a+1]:
            if value[a] not in pairs:
                pairs.append(value[a])
    if len(pairs)>=2:
        return False
    else:
        return True


def password_invalid(value):
    if password_contains_charas(value):
        return True
    if password_doesnt_contain_triple(value):
        return True
    if password_doesnt_have_two_pairs(value):
        return True
    return False

while password_invalid(value):
    value = iterate(value)

print ("Answer to part one: ", "".join(value))

while password_invalid(iterate(value)):
    value = iterate(value)

print ("Answer to part two: ", "".join(value))