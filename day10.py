value="1321131112"


turn=1
while turn <= 50:
    # print (turn, "".join(value), str(len(value)))
    # test=input(".. next ..")
    value = list(value)
    position = 0
    output=[]
    while position < len(value):
        offset = 1
        while offset + position < len(value):
            if value[position]==value[position + offset]:
                offset += 1
            else:
                break
        output.append(str(offset))
        output.append(value[position])
        position += offset
    value = "".join(output)
    turn += 1
    if turn == 41:
        first_part = len(value)
    elif turn == 51:
        second_part = len(value)

print ("Answer to first part: ", first_part)
print ("Answer to second part: ", second_part)