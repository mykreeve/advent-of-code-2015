value = 20151125

y = 1
x = 1
maxY = 1
# print (str(x), str(y), str(value))

while True:
    value = (value * 252533) % 33554393
    if (y - 1) < 1:
        x = 1
        y = maxY + 1
        maxY = y
    else: 
        y -= 1
        x += 1
    
    if x==3075 and y==2981:
        print (str(x), str(y), str(value))
        break

    # row 2981, column 3075.