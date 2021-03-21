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

def randomSkill(enemy):
    skills = [1, 2, 3]
    skill = choice(skills)
    if skill == 1:
        return enemy.skill1()
    if skill == 2:
        return enemy.skill2()
    if skill == 3:
        return enemy.skill3()