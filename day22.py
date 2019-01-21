
spells = {'M':53, 'D':73, 'S':113, 'P':173, 'R':229}
spell_prefs = ['M','D','S','P','R']
spell_next = ['D','S','P','R','M']

spell_order = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']

def iterate_spell_order(pos):
    spell_order[pos] = spell_next[spell_prefs.index(spell_order[pos])]
    if spell_order[pos] == 'M':
        if pos+1 <= len(spell_order):
            iterate_spell_order(pos+1)

def play_game(n):
    playerHP = 50
    playerMana = 500
    playerArmor = 0
    playerEffects = {'S':0, 'R':0}
    bossHP = 71
    bossDamage = 10
    bossEffects = {'P':0}
    spent_mana = 0
    # print ("".join(spell_order))
    for a in spell_order:
        playerHP -= n
        if playerEffects['S']==0:
            playerArmor=0
        elif playerEffects['S']>0:
            playerEffects['S'] -= 1
            playerArmor=7
        if playerEffects['R']>0:
            playerEffects['R'] -= 1
            playerMana += 101
        if bossEffects['P']>0:
            bossEffects['P'] -= 1
            bossHP -= 3

        playerMana -= spells[a]
        spent_mana += spells[a]
        if a == 'M':
            bossHP -= 4
        elif a == 'D':
            bossHP -= 2
            playerHP += 2
        elif a == 'S' and playerEffects['S']==0:
            playerEffects['S']=6
        elif a == 'S':
            # print ("shield already on")
            return 9999
        elif a == 'P' and bossEffects['P']==0:
            bossEffects['P']=6
        elif a == 'P':
            # print ("poison already on")
            return 9999
        elif a == 'R' and playerEffects['R']==0:
            playerEffects['R']=5
        elif a == 'R':
            # print ("recharge already on")
            return 9999

        if playerMana < 0:
            # print ("out of mana")
            return 9999
        if bossHP <= 0:
            # print ("boss dead")
            return spent_mana

        if playerEffects['S']==0:
            playerArmor=0
        elif playerEffects['S']>0:
            playerEffects['S'] -= 1
            playerArmor=7
        if playerEffects['R']>0:
            playerEffects['R'] -= 1
            playerMana += 101
        if bossEffects['P']>0:
            bossEffects['P'] -= 1
            bossHP -= 3

        if bossHP <= 0:
            # print ("boss dead")
            return spent_mana
        playerHP -= max((bossDamage - playerArmor),1)
        if playerHP <= 0:
            # print ("player dead")
            return 9999
        # print (str(playerHP), str(playerMana), str(playerArmor), str(bossHP), a, str(playerEffects), str(bossEffects))

while True:
    result = play_game(0)
    if result != 9999:
        break
    iterate_spell_order(0)

print ("Answer for part one : " + str(result))

highest_mana = 1800
while True:
    result = play_game(1)
    if result != 9999:
        print (result)
    if result != 9999 and result > highest_mana:
        highest_mana = result
    iterate_spell_order(0)