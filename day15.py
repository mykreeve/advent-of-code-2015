filename="input/day15input.txt"
file=open(filename,"r")
file=file.readlines()

ingredients = {}
for item in file:
    item=item.strip().replace(': capacity ',',').replace(', durability ',',').replace(', flavor ',',').replace(', texture ',',').replace(', calories ',',').split(',')
    ingredients[item[0]]={'capacity':int(item[1]), 'durability':int(item[2]), 'flavor': int(item[3]), 'texture': int(item[4]), 'calories': int(item[5])}

def evaluate_cookie(su, sp, ca, ch, max):
    cap = su*ingredients['Sugar']['capacity'] + sp*ingredients['Sprinkles']['capacity'] + ca*ingredients['Candy']['capacity'] + ch*ingredients['Chocolate']['capacity']
    dur = su*ingredients['Sugar']['durability'] + sp*ingredients['Sprinkles']['durability'] + ca*ingredients['Candy']['durability'] + ch*ingredients['Chocolate']['durability']
    fla = su*ingredients['Sugar']['flavor'] + sp*ingredients['Sprinkles']['flavor'] + ca*ingredients['Candy']['flavor'] + ch*ingredients['Chocolate']['flavor']
    tex = su*ingredients['Sugar']['texture'] + sp*ingredients['Sprinkles']['texture'] + ca*ingredients['Candy']['texture'] + ch*ingredients['Chocolate']['texture']
    cal = su*ingredients['Sugar']['calories'] + sp*ingredients['Sprinkles']['calories'] + ca*ingredients['Candy']['calories'] + ch*ingredients['Chocolate']['calories']
    if cap < 0:
        cap = 0
    if dur < 0:
        dur = 0
    if fla < 0:
        fla = 0
    if tex < 0:
        tex = 0
    if cal < 0:
        cal = 0
    if max == 0:
        return (cap * dur * fla * tex)
    else:
        if (cal == max):
            return (cap * dur * fla * tex)
        else:
            return 0

best_score = 0
for sugar in range(101):
    for sprinkles in range(101):
        for candy in range(101):
            for chocolate in range(101):
                if (sugar + sprinkles + candy + chocolate) == 100:
                    score = evaluate_cookie(sugar, sprinkles, candy, chocolate, 0)
                    # if score > 0:
                    #     print ("legit combo - sugar: " + str(sugar) + ", sprinkles: " + str(sprinkles) + ", candy: " + str(candy) + ", chocolate: " + str(chocolate) + " == score: " + str(score))
                    if score > best_score:
                        best_score = score

print ("Answer for part one: " + str(best_score))

best_score = 0
for sugar in range(101):
    for sprinkles in range(101):
        for candy in range(101):
            for chocolate in range(101):
                if (sugar + sprinkles + candy + chocolate) == 100:
                    score = evaluate_cookie(sugar, sprinkles, candy, chocolate, 500)
                    # if score > 0:
                    #     print ("legit combo - sugar: " + str(sugar) + ", sprinkles: " + str(sprinkles) + ", candy: " + str(candy) + ", chocolate: " + str(chocolate) + " == score: " + str(score))
                    if score > best_score:
                        best_score = score

print ("Answer for part two: " + str(best_score))