class Equipment:
    def __init__(self, inventory):
        self.inventory = inventory
        self.head = None
        self.chest = None
        self.shoulder = None
        self.shoes = None
        self.hands = None
        self.gloves = None
        self.legs = None
        self.first_weapon = None
        self.trinket = None

    def takeoff_item(self, slot):
        if slot == 'head':
            self.inventory.add_item(self.head)
            self.head = None
        elif slot == 'shoulder':
            self.inventory.add_item(self.shoulder)
            self.shoulder = None
        elif slot == 'chest':
            self.inventory.add_item(self.chest)
            self.chest = None
        elif slot == 'hands':
            self.inventory.add_item(self.hands)
            self.hands = None
        elif slot == 'gloves':
            self.inventory.add_item(self.gloves)
            self.gloves = None
        elif slot == 'legs':
            self.inventory.add_item(self.legs)
            self.legs = None

        elif slot == 'shoes':
            self.inventory.add_item(self.shoes)
            self.shoes = None

        elif slot == 'weapon':
            self.inventory.add_item(self.first_weapon)
            self.first_weapon = None

    def equip(self, item):
        if (item.sub_type == "Голова") and (self.head is None):
            self.takeoff_item("head")
            self.head = item
            self.inventory.drop_item(item)
        elif (item.sub_type == "Наплечник") and (self.shoulder is None):
            self.takeoff_item("shoulder")
            self.shoulder = item
            self.inventory.drop_item(item)
        elif (item.sub_type == "Нагрудник") and (self.chest is None):
            self.takeoff_item("chest")
            self.chest = item
            self.inventory.drop_item(item)
        elif (item.sub_type == "Перчатки") and (self.gloves is None):
            self.takeoff_item("gloves")
            self.gloves = item
            self.inventory.drop_item(item)
        elif (item.sub_type == "Наруч") and (self.hands is None):
            self.takeoff_item("hands")
            self.hands = item
            self.inventory.drop_item(item)
        elif (item.sub_type == "Штаны") and (self.legs is None):
            self.takeoff_item("legs")
            self.legs = item
            self.inventory.drop_item(item)
        elif item.sub_type == "Обувь" and (self.shoes is None):
            self.takeoff_item("shoes")
            self.shoes = item
            self.inventory.drop_item(item)
        elif item.type == "Оружие" and (self.first_weapon is None):
            self.takeoff_item("weapon")
            self.first_weapon = item
            self.inventory.drop_item(item)
        else:
            print('Ты чего-то перепутал, данный слот уже занят либо предмет кривой ;/')


