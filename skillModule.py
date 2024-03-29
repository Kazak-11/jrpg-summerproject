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
            if random.random() < player.dexWithArmor * 1.5+player.intWithArmor + 15:
                return True
        elif player.passive[0] == 'perfect magic':
            return False
        elif random.random() < player.dexWithArmor * 1.5 + 15:
            return True
        else:
            for effect in player.effect:
                if effect.type == 11 and effect.turns >=1:
                    return True
            return False

class Run_Back(Skill):
    def __init__(self):
        Skill.__init__(self)
    def use(self, battle, player, mob):
        battle.range += player.dexWithArmor

class Run_Forwarfd(Skill):
    def __init__(self):
        Skill.__init__(self)
    def use(self, battle, player, mob):
        battle.range -= player.dexWithArmor

class Runaway(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Run'
        self.name = 'Run'
        self.useDesc = 'Вы сбежали от битвы'
        self.minrange = 30
    def use(self, battle, player, mob):
        Skill.use(self, battle, player, mob)
        battle.run = True

class Shot(Skill):
    def __init__(self):
        Skill.__init__(self)
        self.description = 'Shot'
        self.name = 'Shot'
        self.useDesc = 'Вы нанесли 20 урона'
    def use(self, battle, player, mob):
        for effect in player.effects:
            if effect.type == 12 and effect.turns >= 1:
                for i in range(effect.strength):
                    if Skill.use(self, battle, player, mob):
                        damage = player.dexWithArmor + 20
                        for effect in mob.effects:
                            if effect.type == 10:
                                damage *= (100+effect.strength)/100
                                break
                            elif effect.type == 5 and effect.turns >=1:
                                damage *= (100 + effect.strength) / 100
                                break
                        if self.critical(player):
                            damage*=2
                        mob.take_damage(damage)














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