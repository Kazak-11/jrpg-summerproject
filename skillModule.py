import random
import effectsModule as effects

class Skill():
    def __init__(self):
        self.cost = 0
        self.description = ''
        self.name = ''
        self.useDesc = ''
        self.passive = False
        self.maxrange = 0
        self.minrange = 0
    def print(self, i):
        if i>=0:
            print(str(i)+') '+self.description)
        else:
            print(self.description)
    def use(self, battle, player, mob):
        player.mana -= self.cost
        if random.random() < mob.evade + 0.15: #Уклонение от скилла
            print('Враг уклонился')
            return False
        else:
            return True
    def critical(self, player):
        if player.passive[0] == 'battle art':
            if random.random() < player.dexWithArmor * 1.5 + 15:
        elif player.passive[0] == 'perfect magic':
            return False
        elif random.random() < player.dexWithArmor * 1.5 + 15:
            return True
        else:
            return False

class Mark(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Mark'
        self.name = 'Mark'
        self.useDesc = 'Mark'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            if self.mob.turns(self, self.player):
                effects.mark(3, mob, 65)

class Amining(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.count = 1
        self.boost = 15
        self.arrow = 20
        self.maxstrarrow = 20
        self.buffer = True
        self.buffer2 = True
        self.description = 'Shot'
        self.name = 'Shot'
        self.useDesc = 'Вы нанесли 45 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            if self.mob.turns(self, self.player) and self.buffer:
                self.arrow += self.boost
                self.buffer = False
                if self.buffer2:
                    self.arrow = self.maxstrarrow

class Three_shots(Amining):
    def __init__(self):
        Skill.__init__(self)
        self.count = 1
        self.buffer1 = True
        self.description = 'Shot'
        self.name = 'Shot'
        self.useDesc = 'Вы нанесли 45 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob) and self.buffer1:
            self.count = 3
            if self.buffer2 == True:
                self.buffer1 = False
        if self.buffer1 == False:
            self.count = 1


class Rate_of_fire(Three_shots):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Shot'
        self.name = 'Shot'
        self.buffer3 = True
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            if self.mob.turns(self, self.player):
                self.shoot_speed = (self.arrow*player.int)/5


class Shot(Rate_of_fire):
    def __init__(self):
        Skill.__init__(self)
        self.buffer2 = True
        self.description = 'Shot'
        self.name = 'Shot'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob) and self.buffer3 == False:
            mob.hp -= self.arrow*self.count
            if self.buffer3:
                mob.hp -= self.arrow*self.count+self.shoot_speed
                self.buffer3 = False

class Strong_beat(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Fireball'
        self.name = 'Fireball'
        self.useDesc = 'Вы нанесли 20 урона'
        self.strong_beat = 65
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            mob.hp -= self.strong_beat
            mob.armor -= mob.armor*0.2

class Death_blow(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Fireball'
        self.name = 'Fireball'
        self.useDesc = 'Вы нанесли 20 урона'
        self.strong_beat = 65
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            mob.hp -= mob.hp

class Magic_shield(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Fireball'
        self.name = 'Fireball'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            minor_life = player.hp
            self.player.hp = minor_life

class Magic_arrow(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Fireball'
        self.name = 'Fireball'
        self.useDesc = 'Вы нанесли 20 урона'
        self.magic_arrow = 7
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            player.hp -= self.magic_arrow*5

class Random_magic(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Fireball'
        self.name = 'Fireball'
        self.useDesc = 'Вы нанесли 20 урона'
        self.magic_arrow = 7
    def use(self, battle, player, mob):
        r = random.randint(0, 100):
        for(i in range(1,r))
            if Skill.use(self,battle, player, mob):
                random.choise()

class Run(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Run'
        self.name = 'Run'
        self.useDesc = 'Вы сбежали от битвы'
    def use(self, battle, player, mob):
        Skill.use(self, battle, player, mob)
        battle.run = True

class Attack(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Attack'
        self.name = 'Attack'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            mob.hp -= 5*player.str


class AttackWithStun(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Stun'
        self.name = 'Stun'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            mob.hp -= 3*player.str
            effects.Stun(2, mob)

class Fireball(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Fireball'
        self.name = 'Fireball'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            mob.hp -= 3*player.int
            effects.Fire(3,mob,20)


class Poisonous_smell(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Poisonous smell'
        self.name = 'Poisonous smell'
        self.useDesc = 'Вы нанесли'# + str(self.player.int)*str(self.player.dex) + 'урона'
    def use(self, battle, player, mob):
        if Skill.use(self, battle, player, mob):
            mob.hp -= player.int * player.dex
            effects.Poison(3, mob, 12)

class Firebolt(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Firebolt'
        self.name = 'Firebolt'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self, battle, player, mob):
            mob.hp -= player.str * player.dex
            effects.Fire(3, player, 3)

class Skip(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Skipp'
        self.name = 'Skipp'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        x = 0

class IceLance(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'IceLance'
        self.name = 'IceLance'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            mob.hp -= 3*player.int
            effects.Ice(3,mob)

class Heal(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Heal'
        self.name = 'Heal'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        if Skill.use(self,battle, player, mob):
            effects.Heal(3,player, 10)