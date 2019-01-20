filename="input/day8input.txt"
file=open(filename,"r")
file=file.readlines()

code=0
literal=0
encoded=0

for item in file:
    length = len(item)
    code += length

    listed = list(item)
    reconstructed = []
    n=0
    while n < len(listed):
        if listed[n]=="\\":
            if listed[n+1]=="\\":
                reconstructed.append(listed[n+1])
                n += 2
            elif listed[n+1]=="\"":
                reconstructed.append(listed[n+1])
                n += 2
            elif listed[n+1]=="x":
                reconstructed.append(listed[n+3])
                n += 4
            else:
                reconstructed.append(listed[n])
                n += 1
        else:
            reconstructed.append(listed[n])
            n += 1

    reconstructed = "".join(reconstructed)

    literal += len(reconstructed)
    literal -= 2

print ("Answer to part one: " + str(code-literal))


for item in file:
    item.strip()
    length = len(item)
    listed = list(item)
    reconstructed = ["\""]
    n=0
    while n < len(listed):
        if listed[n]=="\\" and listed[n+1] == "x" and listed[n+2] in '1234567890abcdef' and listed[n+3] in '1234567890abcdef':
            reconstructed.append("\\")
            reconstructed.append("\\")
            reconstructed.append("x")
            reconstructed.append(listed[n+2])
            reconstructed.append(listed[n+3])
            n += 4
        elif listed[n]=="\\":
            reconstructed.append("\\")
            reconstructed.append("\\")
            n += 1
        elif listed[n]=="\"":
            reconstructed.append("\\")
            reconstructed.append("\"")
            n += 1
        else:
            reconstructed.append(listed[n])
            n += 1

    reconstructed.append("\"")

    reconstructed = "".join(reconstructed)

    encoded += len(reconstructed)

print ("Answer to part two: " + str(encoded-code))