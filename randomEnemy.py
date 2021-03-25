from random import choice
import sys
sys.path.append("enemys")

import anthropomorph, beast, dragon

def randomEnemy(lvl):
    enemys = [1, 2, 3]
    enemy = choice(enemys)
    if enemy == 1:
        return anthropomorph.anthropomorph(lvl)
    if enemy == 2:
        return beast.beast(lvl)
    if enemy == 3:
        return dragon.dragon(lvl)

def enemyList(lvl, count):
    enemy = randomEnemy(lvl)
    lst = []
    if enemy.type == "Зверь":
        for i in range(count):
            lst.append(beast.beast(lvl))

    if enemy.type == "Дракон":
        for i in range(count):
            lst.append(dragon.dragon(lvl))
    
    if enemy.type == "Антропоморф":
        for i in range(count):
            lst.append(anthropomorph.anthropomorph(lvl))
    
    return lst