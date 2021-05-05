from random import choice
import enemies.anthropomorph as anthropomorph
import enemies.beast as beast
import enemies.dragon as dragon

def randomEnemy(lvl):
    enemys = [1, 2, 3, 1, 2]
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