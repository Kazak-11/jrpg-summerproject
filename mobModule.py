import random
import effectsModule as effects

class Mob():  #Базовый класс моба, имеющий
    def __init__(self):
        self.str = 0
        self.dex = 0
        self.evade = -0.15
        self.exp = 0
        self.stop = False
        self.effects = []
        self.hp = 0
        self.maxhp = 0
    def turn(self, battle, player):
        i = 0
        for effect in self.effects:
            effect.use(self, i)
            i+=1
        if battle.sneak:
            print('Монстр вас не видит')
            return False
        else:
            if not self.stop and self.hp > 0:
                return True
            elif self.stop:
                print('Враг оглушен')
                self.stop = False
                return False
            else:
                return False
    def deal_damage(self,player, n):
        if random.random()< (player.dexWithArmor + 15)/100 and player.passive[0]!='total defence':
            print('Вы уклонились')
        else:
            player.hp-= n
            print('Вы получили '+n+' урона')
    def take_damage(self, n):
        if random.random() > self.dex*2:
            self.hp -= n



class Bear(Mob):
    def __init__(self):
        Mob.__init__(self)
        self.hp = 100
        self.maxhp = self.hp
        self.exp = 100
    def turn(self,battle, player):
        Mob.turn(self, battle, player)

class Bear2(Mob):
    def __init__(self):
        Mob.__init__(self)
        self.hp = 200
        self.str = 15
        self.maxhp = self.hp
        self.exp = 100
        self.buffer = True
        self.buffer1 = True
        self.bufferp =True
    def turn(self,battle, player):
        if Mob.turn(self, battle, player):
            if battle.range > 2:
                battle.range-=10
            else:
                if self.hp < self.maxhp*0.3:
                    if self.buffer:
                        effects.Heal(3, self, 10)
                        self.buffer = False
                if self.hp < self.maxhp*0.5:
                    if self.buffer1:
                        effects.Fire(2, player, 20)
                        self.buffer1 = False