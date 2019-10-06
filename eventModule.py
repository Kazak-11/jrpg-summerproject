import itemsModule as items
from random import randrange

class Event():   #Класс событий с общим интерфейсом
    def __init__(self, player, init):
        self.player = player


class Trade(Event):
    def __init__(self, player, lvl):
        Event.__init__(self, player, 0)
        self.player = player
        self.items = [items.RandomClothes(lvl), items.RandomClothes(lvl), items.RandomClothes(lvl)]
    def deal(self):
        action = -1
        while action != 0:
            i = 1
            print('Продается:')
            for item in self.items:
                print(str(i)+') '+item.desc+' стоит '+str(item.price*2))
                print('Armor = ' + item.armor.__str__() + ', str = ' + item.str.__str__() + ', dex = ' +
                      item.dex.__str__() + ', int = ' + item.int.__str__() + ', mana = ' + item.mana.__str__())
                i += 1
            print('У вас '+str(self.player.money)+' монет')
            print('В инвентаре:')
            i = 1
            for item in self.player.inventory:
                print(str(i)+') '+item.desc+' стоит '+str(item.price))
                print('Armor = ' + item.armor.__str__() + ', str = ' + item.str.__str__() + ', dex = ' +
                      item.dex.__str__() + ', int = ' + item.int.__str__() + ', mana = ' + item.mana.__str__())
                i += 1
            print('Введите номер покупки или i+номер продажи(i2, например). Чтобы выйти введите 0')
            action = input()
            char = action[0:1]
            if char == 'i': #Если i, то продается из инвенторя предмет
                action = action[1::]
                self.player.money += self.player.inventory[int(action)-1].price
                del self.player.inventory[int(action)-1]
            elif action == '0': #Выход из торговли
                break
            elif self.player.money>= self.items[int(action)-1].price*2: #Покупка предмета
                self.player.money -= self.items[int(action)-1].price*2
                self.player.inventory.append(self.items[int(action)-1])
                del self.items[int(action)-1]



class Battle(Event):
    def __init__(self ,player ,init , mob):
        Event.__init__(self, player, init)
        self.init = init
        self.mob = mob
        self.run = False
        self.range = randrange(0, (player.intWithArmor * 0.1 + player.dexWithArmor * 0.25) * 70)
        self.player.mana = self.player.maxmana
        if player.passive[0] == 'sneak':
            self.sneak = True
    def writeActions(self, list): #Выводит список действий возможных
        i = 0
        for action in list:
            action.print(i)
            i+=1
    def readAction(self, list): #Считывает введенное действие
        answer = int(input())
        if answer > len(list) or answer < 0:
            return False
        else:
            return list[answer]
    def pTurn(self): #Происходит ход игрока, выводятся его хар-ки, совершается действие(если хватает маны)
        i = 0
        for effect in self.player.effects: #Проверка эффектов на игроке
            effect.use(self.player, i)
            i += 1
        self.player.mana += self.player.maxmana*0.1
        if not self.player.stop: #Проверка на стан
            action = False
            while action!=True:
                print('Enemy HP='+str(self.mob.hp))
                print('Your HP=' + str(self.player.hp))
                print('Your Armor=' + str(self.player.armor))
                print('Your Mana=' + str(self.player.mana))
                self.writeActions(self.player.skills)
                skill = self.readAction(self.player.skills)
                if skill.cost<=self.player.mana and skill.minrange<=self.range and self.range <=skill.maxrange:
                    skill.use(self, self.player, self.mob) #Использует скилл
                    action = True
                else:
                    print('Вам не хватает маны')
        else:
            self.player.stop = False

    def loop(self):
        if self.init == 1 and self.player.passive[0] == 'initiative': #Если у игрока инициатива, то перед зацикленным боем проводится его дополнительный ход
            self.pTurn()
        if not self.run:
            while self.mob.hp >0: #Пока кто-нибудь не умер или игрок не убежал
                self.mob.turn(self, self.player)
                if self.player.hp<=0:
                    print('YOU DIED')
                    break
                self.pTurn()
                if self.run == True:
                    return False
        return True