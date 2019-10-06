import itemsTable as items
import random

class Item():
    def __init__(self):
        self.desc = ''

class Clothes(Item):
    def __init__(self):
        Item.__init__(self)
        self.wearable = True
        self.place = -1
        self.empty = False
        self.armor = 0
        self.str = 0
        self.int = 0
        self.dex = 0
        self.mana = 0
    def use(self, player): #Заменяет экипированный предмет на этот
        if player.equip[self.place] and not player.equip[self.place].empty:
            player.inventory.append(player.equip[self.place])
        player.equip[self.place] = self
        player.inventory.remove(self)
    def remove(self, player): #Убирает эк.предмет в инвентарь и создает пустышку
        if player.equip[self.place] and not player.equip[self.place].empty:
            player.inventory.append(player.equip[self.place])
            player.equip[self.place] = Empty(self.place)


class Empty(Clothes): #Пустышка
    def __init__(self,place):
        Clothes.__init__(self)
        self.place = place
        self.empty = True


class Things():
    def __init__(self):
        self.wearable = False

class GreatBoots(Clothes): #НАГРУДНИК КОТОРЫЙ САПОГИ
    def __init__(self):
        Clothes.__init__(self)
        self.place = 1
        self.armor = 100
        self.price = 100
        self.desc = 'Лучшие сапоги мира'

class RandomClothes(Clothes): #Рандомный предмет, созданный из таблицы предметов
    def __init__(self, level):
        Clothes.__init__(self)
        self.place = random.randrange(0,5)
        self.armor = random.randrange(items.armor[self.place][level][0],items.armor[self.place][level][1])
        self.str = random.randrange(items.armor[self.place][level][2], items.armor[self.place][level][3])
        self.int = random.randrange(items.armor[self.place][level][2], items.armor[self.place][level][3])
        self.dex = random.randrange(items.armor[self.place][level][2], items.armor[self.place][level][3])
        self.mana = random.randrange(items.armor[self.place][level][4], items.armor[self.place][level][5])
        self.desc = items.armor[self.place][level][6]
        self.price = 10

