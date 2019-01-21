filename="input/day21input.txt"
file=open(filename,"r")
file=file.readlines()

boss={}

for line in file:
    line=line.strip().replace(': ',',').replace(' ','').split(',')
    boss[line[0]]=int(line[1])

weapons = [('Dagger',8,4,0), ('Shortsword',10,5,0), ('Warhammer',25,6,0), ('Longsword',40,7,0), ('Greataxe',74,8,0)]
armors = [('None',0,0,0), ('Leather',13,0,1), ('Chainmail',31,0,2), ('Splintmail',53,0,3), ('Bandedmail',75,0,4), ('Platemail',102,0,5)]
rings = [('None',0,0,0), ('None',0,0,0), ('Damage + 1',25,1,0), ('Damage + 2',50,2,0), ('Damage + 3',100,3,0), ('Defense + 1',20,0,1), ('Defense + 2',40,0,2), ('Defense + 3',80,0,3)]

def do_battle(dam, res):
    playerHP = 100
    playerDamage = dam
    playerResist = res
    bossHP = boss['HitPoints']
    bossDamage = boss['Damage']
    bossResist = boss['Armor']
    playerTurnDamage = playerDamage-bossResist
    if playerTurnDamage < 1:
        playerTurnDamage = 1
    bossTurnDamage = bossDamage-playerResist
    if bossTurnDamage < 1:
        bossTurnDamage = 1
    while True:
        bossHP = bossHP-playerTurnDamage
        if bossHP <= 0:
            return "player"
        playerHP = playerHP-bossTurnDamage
        if playerHP <= 0:
            return "boss"

worst_cost = 0
best_cost = 10000

for weapon in weapons:
    for armor in armors:
        for n1, ring1 in enumerate(rings):
            for n2, ring2 in enumerate(rings):
                if n1 != n2:
                    cost = weapon[1]+armor[1]+ring1[1]+ring2[1]
                    damage = weapon[2]+ring1[2]+ring2[2]
                    resist = armor[3]+ring1[3]+ring2[3]

                    result = do_battle(damage, resist)
                    if result == "boss":
                        # print ("BOSS WON.", weapon[0], armor[0], ring1[0], ring2[0])
                        if cost > worst_cost:
                            worst_cost = cost
                            # print ("Cost of defeat was the highest yet - " + str(cost))
                    if result == "player":
                        # print ("PLAYER WON.", weapon[0], armor[0], ring1[0], ring2[0])
                        if cost < best_cost:
                            best_cost=cost
                            # print ("Cost of victory was the lowest yet - " + str(cost))

print ("Answer to part one: " + str(best_cost))
print ("Answer to part two: " + str(worst_cost))