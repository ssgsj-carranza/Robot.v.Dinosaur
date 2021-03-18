class Robot:
    def __init__(self):
        self.name = "voltron"
        self.health = "250"
        self.power_level = "400"
        self.weapon = "sword"
        self.attack_power = "50"
class Dinosaur:
    def __init__(self):
        self.type = "Metal-Greymon"
        self.health = "180"
        self.energy = "500"
        self.attack_power = "100"
class Fleet:
    def __init__(self):
        self.robots = list()
        self.robots.append(Robot())
        self.robots.append(Robot())
        self.robots.append(Robot())
    def defeated(self):
        for robot in self.robots:
            if robot.health > 0:
                return False
        return True
class Herd:
    def __init__(self):
        self.dinosaurs = list()
        self.dinosaurs.append(Dinosaur())
        self.dinosaurs.append(Dinosaur())
        self.dinosaurs.append(Dinosaur())

# class Weapon:
# class Battlefield:

def fightSequence():
    robot = Fleet()
    dinosaur = Herd()
    encounter = 1
    turn = 'Dinosaur'
    while encounter == 1:
        if turn == 'Dinosaur':
            action = input("What would you like to do (Attack)? ")
            if action == 'Attack':
                encounter = humanAttack(Player)
                turn = 'monster'
        elif turn == 'monster':
            encounter = monsterAttack(Monster)
            turn = 'player'


fightSequence()