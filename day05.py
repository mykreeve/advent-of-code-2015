filename="input/day5input.txt"
file=open(filename,"r")
file=file.readlines()

nice=0
naughty=0

def contains_three_vowels(text):
    text=list(text)
    vowels=0
    for c in text:
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            vowels+=1
    if vowels >= 3:
        return True
    else:
        return False

def contains_double(text):
    text=list(text)
    for n,c in enumerate(text):
        if n!=len(text)-1:
            if c==text[n+1]:
                return True
    return False

def not_contain(text):
    if 'ab' in text:
        return False
    if 'cd' in text:
        return False
    if 'pq' in text:
        return False
    if 'xy' in text:
        return False
    return True

def check(text):
    if (contains_three_vowels(text) and contains_double(text) and not_contain(text)):
        return True
    else:
        return False

for line in file:
    line=line.strip()
    if check(line):
        nice += 1
    else:
        naughty += 1

print ("Answer to part one:")
print ("Nice: " + str(nice) + ", Naughty: " + str(naughty))

nice=0
naughty=0

def contains_pair_twice(text):
    text=list(text)
    for a in range(len(text)-2):
        search_text=text[a]+text[a+1]
        for b in range(a+2,len(text)-1):
            if text[b]+text[b+1]==search_text:
                return True
    return False

def split_pair(text):
    text=list(text)
    for a in range(len(text)-2):
        if text[a]==text[a+2]:
            return True
    return False

def second_check(text):
    if (contains_pair_twice(text) and split_pair(text)):
        return True
    else:
        return False

for line in file:
    line=line.strip()
    if second_check(line):
        nice += 1
    else:  
        naughty += 1

print ("Answer to part two:")
print ("Nice: " + str(nice) + ", Naughty: " + str(naughty))