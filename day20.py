target=36000000

testValue=2520
total=0
while True:
    total=0
    for a in range(1, testValue+1):
        if testValue % a == 0:
            total += (a*10)
    if total > target:
        print ("Answer to part one: " + str(testValue))
        break
    testValue += 2520

testValue=2520
total=0
while True:
    total=0
    for a in range(1, testValue+1):
        if (testValue % a == 0) and (testValue/a < 50):
            total += (a*11)
    if total > target:
        print ("Answer to part two: " + str(testValue))
        break
    testValue += 2520
