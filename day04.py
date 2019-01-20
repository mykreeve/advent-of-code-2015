import hashlib

input="yzbqklnj"
value=1
found=False

while True:
    test=(input+str(value)).encode('utf-8')
    test=hashlib.md5(test).hexdigest()
    if test[:6]=='000000':
        print ("Answer to part two: " + str(value))
        break
    if test[:5]=='00000' and found==False:
        print ("Answer to part one: " + str(value))
        found=True
    value += 1
