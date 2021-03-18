class Robot:
    def __init__(self):
        self.name = "voltron"
        self.health = 250
        self.power_level = 400
        self.weapon = "sword"
        self.attack_power = 50
class Dinosaur:
    def __init__(self):
        self.type = "Metal-Greymon"
        self.health = 180
        self.energy = 500
        self.attack_power = 100


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

    def defeated(self):
        for dino in self.dinosaurs:
            if dino.health > 0:
                return False
        return True

# class Weapon:
# class Battlefield:


def fight_sequence():
    robot = Fleet()
    dinosaur = Herd()
    turn = 'Dinosaur'
    while not robot.defeated() and not dinosaur.defeated():
        if turn == 'Dinosaur':
            for robot in robot.robots:
                robot.health -= dinosaur.dinosaurs[0].attack_power
            turn = 'Robot'
        elif turn == 'Robot':
            for dinosaur in dinosaur.dinosaurs:
                dinosaur.health -= robot.robots[0].attack_power
            turn = 'Dinosaur'
    print(robot.defeated())
    print(dinosaur.defeated())


fight_sequence()