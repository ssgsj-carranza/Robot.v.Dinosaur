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

#this function loops through the fight sequence


def fight_sequence():
    robotOne = Fleet()
    dinosaurOne = Herd()
    turn = 'Dinosaur'
    while not robotOne.defeated() and not dinosaurOne.defeated():
        if turn == 'Dinosaur':
            for robot in robotOne.robots:
                robot.health -= dinosaurOne.dinosaurs[0].attack_power
            turn = 'Robot'
        elif turn == 'Robot':
            for dinosaur in dinosaurOne.dinosaurs:
                dinosaur.health -= robotOne.robots[0].attack_power
            turn = 'Dinosaur'
    print("The dinosaurs won: ", robotOne.defeated())
    print("The robots won: ", dinosaurOne.defeated())


fight_sequence()

