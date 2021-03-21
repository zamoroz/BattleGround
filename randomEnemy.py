from random import choice
import sys
sys.path.append("enemys")

import antropomorph, beast, dragon

def randomEnemy(lvl):
    enemys = [1, 2, 3]
    enemy = choice(enemys)
    if enemy == 1:
        return antropomorph.antropomorph(lvl)
    if enemy == 2:
        return beast.beast(lvl)
    if enemy == 3:
        return dragon.dragon()