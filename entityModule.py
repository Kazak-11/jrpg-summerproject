import mobModule as mobs
import classModule as roles
import eventModule as events
import itemsModule as items
import mapModule as maps

class Entity(): #Класс сущности, имеет координаты, обозначение и метод перемещения
    def __init__(self, entMap, x, y):
        self.x = x
        self.y = y
        self.mark = '+'
        self.map = entMap
        self.map[self.x][self.y] = self
    def turn(self):
        x = 0
    def trigger(self, another):
        x = 0
    def move(self, way): #Пытается перейти на другую клетку, если на ней есть сущность, то вызывает триггер взаимодействия
            if way == 'w' and self.x > 0:
                if self.map[self.x - 1][self.y] == '+':
                    self.map[self.x][self.y] = '+'
                    self.x = self.x - 1
                    self.map[self.x][self.y] = self
                else:
                    self.trigger(self.map[self.x - 1][self.y])
            elif way == 's' and self.x < len(self.map) - 1:
                if self.map[self.x + 1][self.y] == '+':
                    self.map[self.x][self.y] = '+'
                    self.x = self.x + 1
                    self.map[self.x][self.y] = self
                else:
                    self.trigger(self.map[self.x + 1][self.y])
            elif way == 'a' and self.y > 0:
                if self.map[self.x][self.y - 1] == '+':
                    self.map[self.x][self.y] = '+'
                    self.y = self.y - 1
                    self.map[self.x][self.y] = self
                else:
                    self.trigger(self.map[self.x][self.y - 1])
            elif way == 'd' and self.y < len(self.map) - 1:
                if self.map[self.x][self.y + 1] == '+':
                    self.map[self.x][self.y] = '+'
                    self.y = self.y + 1
                    self.map[self.x][self.y] = self
                else:
                    self.trigger(self.map[self.x][self.y + 1])

class Trader(Entity): #Сущность сундука, имеет уровень продаваемых предметов
    def __init__(self, entMap, x, y, lvl):
        Entity.__init__(self, entMap, x ,y)
        self.role = 'trade'
        self.mark = 'Q'
        self.lvl = lvl

class Chest(Entity): #Сущность сундука, имеет уровень подбираемых предметов
    def __init__(self, entMap, x, y, lvl):
        Entity.__init__(self, entMap, x ,y)
        self.lvl = lvl
        self.role = 'chest'
        self.mark = '#'

class mob(Entity):
    def __init__(self, entMap, x, y):
        Entity.__init__(self, entMap, x, y)
        self.role = 'mob'

class Bear(mob):
    def __init__(self, entMap, x, y):
        mob.__init__(self, entMap, x, y)
        self.mark = 'b'
        self.ref = mobs.Bear()

class Player(Entity): #Класс игрока, имеет хар-ки, ресурсы, методы для изменения хар-ок и для действий на карте
    def __init__(self, entMap, x, y):
        Entity.__init__(self, entMap, x, y)
        self.mark = '@'
        self.hp = 50
        self.maxhp = 100
        self.armor = 0
        self.maxmana = 0
        self.mana = 0
        self.str = 5
        self.dex = 5
        self.int = 5
        self.strWithArmor = 5 #Хар-ки с броней
        self.dexWithArmor = 5
        self.intWithArmor = 5
        self.maxmanaWithArmor = 0
        self.stm = 5
        self.money = 0
        self.exp = 0
        self.lvl = 1
        self.points = 5
        self.skills = [] #Список навыков, полученных игроком
        self.passive = [] #Список пассивок(нереализовано)
        self.effects = [] #Эффекты наложенные на игрока в бою
        self.stop = False #Стан на игроке в бою
        self.lvlList = [0,100, 150, 200, 200, 200] #Список требований опыта для соответствующих уровней
        boots = items.GreatBoots()
        self.inventory = [boots] #Инвентарь
        self.equip = [items.Empty(0),items.Empty(1),items.Empty(2),items.Empty(3),items.Empty(4),items.Empty(5)] #Надетые вещи, изначально пустые
        self.usePoints() #Первичное распределение очков
        self.chooseRole()
        self.chooseSkills() #Первичный выбор навыков
    def cheakArmor(self): #Метод обновляет переменные, связанные с броней, проверяя надетые вещи
        self.armor = 0
        self.strWithArmor = self.str
        self.dexWithArmor = self.dex
        self.intWithArmor = self.int
        self.maxmanaWithArmor = self.maxmana
        for item in self.equip:
            self.armor+=item.armor
            self.strWithArmor = item.str
            self.dexWithArmor = item.dex
            self.intWithArmor = item.int
            self.maxmanaWithArmor = item.mana
        if self.passive[0] == 'total defence':
            self.armor += self.dexWithArmor
    def cheakInventory(self):
        action = -2
        while action != '0': #0 это выход
            i = 1
            print('EXP = '+str(self.exp))
            print('LVL = '+ str(self.lvl))
            print('Armor = '+str(self.armor))
            for item in self.equip:
                print(str(item.place)+') '+item.desc)
                if not item.empty:
                    print('Armor = ' + item.armor.__str__() + ', str = ' + item.str.__str__() + ', dex = ' +
                      item.dex.__str__() + ', int = ' + item.int.__str__() + ', mana = ' + item.mana.__str__())
            print('Введите 0, чтобы выйти без изменений')
            for item in self.inventory:
                print(str(i)+') '+item.desc)
                print('Armor = ' + item.armor.__str__() + ', str = ' + item.str.__str__() + ', dex = ' +
                      item.dex.__str__() + ', int = ' + item.int.__str__() + ', mana = ' + item.mana.__str__())
                i += 1
            action = input()
            if action[0:1] == 'r': #Снимает предмет
                self.equip[int(action[1::])].remove(self)
            elif int(action) > 0 and int(action) < i+1:
                self.inventory[int(action)-1].use(self) #Пытается использовать предмет
            self.cheakArmor() #Обновляет броню

    def usePoints(self):
        str = self.str
        dex = self.dex
        int = self.int
        stm = self.stm
        answer = ''
        while answer != 'c':  # Пока игрок не начал/продолжил игру
            print('points = ' + self.points.__str__())   #используется __str__(), потому что str это переменная силы
            print('str = ' + str.__str__())
            print('dex =' + dex.__str__())
            print('int = ' + int.__str__())
            print('stm = ' + stm.__str__())
            answer = input()
            if answer != 'c':
                char = answer[0:3]
                way = 0
                if answer[3:4] == '+':  # увеличить хар-ку
                    way = 1
                    if self.points == 0:
                        print('Вы потратили все очки')
                        continue
                elif answer[3:4] == '-':  # уменьшить хар-ку
                    way = -1
                    if char == 'str' and self.str == str:
                        print('Вы не можете опустить характеристики ниже 5')
                        continue
                    elif char == 'dex' and self.dex == dex:
                        print('Вы не можете опустить характеристики ниже 5')
                        continue
                    elif char == 'int' and self.int == int:
                        print('Вы не можете опустить характеристики ниже 5')
                        continue
                    elif char == 'stm' and self.stm == stm:
                        print('Вы не можете опустить характеристики ниже 5')
                        continue
                self.points -= way
                if char == 'str':
                    str += way
                elif char == 'dex':
                    dex += way
                elif char == 'int':
                    int += way
                elif char == 'stm':
                    stm += way
        self.str = str
        self.dex = dex
        self.int = int
        self.stm = stm
    def chooseRole(self): #Выбор роли и присвоение скиллов, связанных с этой ролью игроку
        print('1) Воин')
        print('2) Лучник')
        print('3) Маг')
        print('4) Бомж')
        action = ''
        while action == '':
            action = input('Выберите класс \n')
            if action == '1':
                self.role = roles.Role()
                break
            elif action == '2':
                self.role = roles.Archer()
                break
            elif action == '3':
                self.role = roles.Wizard()
                break
            elif action == '4':
                self.role = roles.Bum()
                break
            action = ''
        self.skills = self.role.skills[0]
    def chooseSkills(self):
        print('Выберите один из следующих скиллов:')
        i = 1
        for skill in self.role.skills[self.lvl]: #Выводит скиллы, относящиеся к нужной роли на нужном уровне
            print(str(i)+') '+skill.description)
            i += 1
        action = int(input()) - 1
        if self.role.skills[self.lvl][action].passive:
            self.passive.append(self.role.skills[self.lvl][action])
        else:
            self.skills.append(self.role.skills[self.lvl][action])
    def trigger(self, another):
        if another.role == 'mob': #Если моб, то создать событие битву
            battle = events.Battle(self, 1, another.ref)
            result = battle.loop()
            if result:
                self.earnExp(another.ref.exp)
                self.map[self.x][self.y] = '+'
                self.x = another.x
                self.y = another.y
                self.map[self.x][self.y] = self
        elif another.role == 'chest': #Если сундук, то выдать предмет
            item = items.RandomClothes(another.lvl)
            print('Вы получили предмет:')
            print(item.desc+', Armor = '+ item.armor.__str__()+', str = '+item.str.__str__()+', dex = '+item.dex.__str__()+', int = '+item.int.__str__()+', mana = '+item.mana.__str__())
            self.inventory.append(item)
            self.map[self.x][self.y] = '+'
            self.x = another.x
            self.y = another.y
            self.map[self.x][self.y] = self
        elif another.role == 'trade': #Если торгаш, то создать событие торговли
            trade = events.Trade(self, another.lvl)
            trade.deal()
    def earnExp(self, exp): #Вызывается для получения опыта, проверяет на повышение уровня
        self.exp += exp
        if self.exp >= self.lvlList[self.lvl]:
            self.lvl += 1
            self.exp = 0
            self.hp = self.maxhp
            self.points += 2
            if len(self.role.skills[self.lvl]) > 0:
                self.chooseSkills() #При каждом определенном повышении уровня нужно выбрать новый скилл
    def action(self, image):
        action = input()
        while action == 'i' or action == 'p': #Открыть инвентарь или меню распределения очков можно сколько раз за ход
            if action == 'i':
                self.cheakInventory()
            elif action == 'p':
                self.usePoints()
            maps.print_array(image)
            action = input()
        if action == 'w' or action == 's' or action == 'a' or action == 'd': #Ходить и взаимодействовать с клетками можно 1 раз в ход
            self.move(action)