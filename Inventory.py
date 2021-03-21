
class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item] = item

    def drop_item(self, item):
        if item.name in self.items:
            self.items.pop(item)

    def use_item(self, item, target=None):
        if item in self.items.values():
            item.use_item(target)

    def __str__(self):
        out = '\t'.join(['Наименование предмета', 'Уровень предмета', 'Используемый?', 'Ловкость', 'Защита предмета',
                         'Здоровье предмета','Тип предмета', 'Подтип предмета', 'Сила предмета' ])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in ([item.name, item.exp, item.applied,
                                                    item.dexterity, item.protection, item.health, item.item_type,
                                                      item.sub_type, item.strenght])])
        return out
