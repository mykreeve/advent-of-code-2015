filename="input/day2input.txt"
file=open(filename,"r")
file=file.readlines()

total_area=0
total_ribbon=0
for line in file:
    line=line.strip().split('x')
    l,w,h=line
    l=int(l)
    w=int(w)
    h=int(h)
    area=(2*l*w) + (2*w*h) + (2*h*l) + min(l*w,w*h,h*l)
    ribbon=(min((2*(l+w)), (2*(w+h)), (2*(h+l))) + (h*w*l))
    total_area += area
    total_ribbon += ribbon

print("Answer to part one: " + str(total_area))
print("Answer to part two: " + str(total_ribbon))