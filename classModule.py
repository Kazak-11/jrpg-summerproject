import skillModule as skills

class Role():
    def __init__(self):
        run = skills.Run()
        attack = skills.Attack()
        stun = skills.AttackWithStun()
        self.skills = [[run, attack], [stun, skills.Fireball()], [skills.Skip(), skills.IceLance()], [skills.Heal()]] #Тестовые скиллы распределенные по уровням

class Warrior(Role):
    def __init__(self):
        Role.__init__(self)

class Archer(Role):
    def __init__(self):
        Role.__init__(self)

class Wizard(Role):
    def __init__(self):
        Role.__init__(self)

class Bum(Role):
    def __init__(self):
        Role.__init__(self)