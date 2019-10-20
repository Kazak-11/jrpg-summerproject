class Effect():    #Базовый класс эффектов, имеет кол-во ходов и тип эффекта
    def __init__(self, turns, target):
        self.turns = turns
        self.type = 0
        target.effects.append(self) #Добавляет эффект цели
    def use(self, target, i): #Уменьшает кол-во оставшихся ходов эффекта или удаляет его(ссылку)
        if self.turns > 1:
            print('Turns =' + str(self.turns) + ', name = ' + str(self.type))
            self.turns -= 1
            return True
        else:
            del target.effects[i]
            return False



class Stun(Effect):
    def __init__(self, turns, target):
        Effect.__init__(self, turns, target)
    def use(self, target, i):
        if Effect.use(self, target, i):
            target.stop = True #Изменяет переменную стана


class  Power_weakening(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self, turns, target, strength)
        self.strength = strength
        self.check(target)
        target.str -= self.strength
        self.type = 7
    def use(self,target, i):
        if Effect.use(self> target, i):
            if target.str < self.strength:
                target.str = 0
        if not Effect.use(self, target, i):
            target.str += self.strength
    def check(self, target):
                for effect in target.effects:
                    if effect.type == 7 and effect.turns > 0:
                        effect.turns += self.turns
                        if effect.strength < self.strength:
                            effect.strength = self.strength
                        self.turns = 0

class Attack_stance(Effect):
    def __init__(self, turns, target):
        Effect.__init__(self, turns, target)
        self.check(target)
        self.type = 8
    def use(self,target, i):
        if Effect.use(self, target, i):
            target.str += target.str*0.25
            target.armor -= target.armor*0.2
    def check(self,target):
        for effect in target.effects:
            if effect.type == 8 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0

class Mark(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self, turns, target, strength)
        self.strength = strength
        self.check(target)
        self.type = 6
    def use(self,target, i):
        if Effect.use(self, target, i):
            target.hp -= self.player.str +self.strength
    def check(self,target):
        for effect in target.effects:
            if effect.type == 1 and effect.turns > 0:
                effect.turns += self.turns
            if effect.strength < self.strength:
                effect.strength = self.strength
                self.turns = 0

class Fire(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self, turns, target)
        self.strength = strength #Сила это кол-во урона в ход
        self.check(target)
        self.type = 1
    def use(self,target, i):
        if Effect.use(self, target, i):
            target.hp -= self.strength
    def check(self,target): #Проверяет есть ли такой же эффект у цели(объединяет) или противоположный(вычитает)
        for effect in target.effects:
            if effect.type == 2 and self.turns > 0:
                buffer = effect.turns
                effect.turns -= self.turns
                self.turns -= buffer
            elif effect.type == 1 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0

class Ice(Effect):
    def __init__(self, turns, target):
        Effect.__init__(self, turns, target)
        self.check(target)
        self.type = 2
    def use(self,target, i):
        if Effect.use(self, target, i):
            target.stop = True
    def check(self,target):
        for effect in target.effects:
            if effect.type == 1 and self.turns > 0:
                buffer = effect.turns
                effect.turns -= self.turns
                self.turns -= buffer
            elif effect.type == 2 and effect.turns > 0:
                effect.turns += self.turns
                self.turns = 0

class Poison(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self, turns, target)
        self.strength = strength
        self.check(target)
        self.type = 3
    def use(self, target, i):
        if Effect.use(self, target, i):
            target.hp -= (self.turns+1)*self.strength #Чем больше ходов яда, тем он сильнее
    def check(self, target):
        for effect in target.effects:
            if effect.type == 4 and self.turns > 0:
                buffer = effect.turns
                effect.turns -= self.turns
                self.turns -= buffer
            elif effect.type == 3 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0

class Heal(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self, turns, target)
        self.strength = strength #Сила влияет на кол-во хила в ход
        self.check(target)
        self.type = 4
    def use(self, target, i):
        if Effect.use(self, target, i):
            target.hp += (self.turns+1)*self.strength
            if target.hp > target.maxhp:
                target.hp = target.max.hp
    def check(self, target):
        for effect in target.effects:
            if effect.type == 3 and self.turns > 0:
                buffer = effect.turns
                effect.turns -= self.turns
                self.turns -= buffer
            elif effect.type == 4 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0

class Time_Mark(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self,turns, target)
        self.strength = strength
        self.check(target)
        self.type = 5
    def use(self, target, i):
        Effect.use(self, target, i)
    def check(self, target):
        for effect in target.effects:
            if effect.type == 5 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0
            elif effect.type == 10 and effect.turns > 0:
                del effect

class Infinity_Mark(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self,0, target)
        self.strength = strength
        self.check(target)
        self.type = 10
    def check(self, target):
        for effect in target.effects:
            if effect.type == 10 and effect.turns > 0:
                if effect.strength < self.strength:
                    effect.strength = self.strength
                del self
            elif effect.type == 5 and effect.turns > 0:
                del effect

class  Weakening(Effect):
    def __init__(self, turns, target, strength, type, char):
        Effect.__init__(self, turns, target)
        self.strength = strength
        self.check(target, type)
        self.type = type
        self.char = char
        if self.char >= self.strength:
            self.char -= self.strength
        else:
            self.buffer = self.char
            self.char = 0
    def use(self,target, i):
        if not Effect.use(self, target, i):
            self.char += self.strength
    def check(self, target, type):
                for effect in target.effects:
                    if effect.type == type and effect.turns > 0:
                        effect.turns += self.turns
                        if effect.strength < self.strength:
                            effect.strength = self.strength
                        self.turns = 0

class Armor_weaking(Weakening):
    def __init__(self, turns, target, strength):
        Weakening.__init__(self, turns, target, strength, 6, target.armor)

class Str_weaking(Weakening):
    def __init__(self, turns, target, strength):
        Weakening.__init__(self, turns, target, strength, 7, target.str)

class Int_weaking(Weakening):
    def __init__(self, turns, target, strength):
        Weakening.__init__(self, turns, target, strength, 8, target.int)

class Dex_weaking(Weakening):
    def __init__(self, turns, target, strength):
        Weakening.__init__(self, turns, target, strength, 9, target.dex)


class Concentration(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self,turns, target)
        self.strength = strength
        self.check(target)
        self.type = 11
    def use(self, target, i):
        Effect.use(self, target, i)
    def check(self, target):
        for effect in target.effects:
            if effect.type == 11 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0

class MultiSkill(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self,turns, target)
        self.strength = strength
        self.check(target)
        self.type = 12
    def use(self, target, i):
        Effect.use(self, target, i)
    def check(self, target):
        for effect in target.effects:
            if effect.type == 12 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0

class TypeOfArrow(Effect):
    def __init__(self, turns, target, strength):
        Effect.__init__(self,turns, target)
        self.strength = strength
        self.check(target)
        self.type = 13
    def use(self, target, i):
        Effect.use(self, target, i)
    def check(self, target):
        for effect in target.effects:
            if effect.type == 13 and effect.turns > 0:
                effect.turns += self.turns
                if effect.strength < self.strength:
                    effect.strength = self.strength
                self.turns = 0