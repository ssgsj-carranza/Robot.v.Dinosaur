import random


class Robot:
    def __init__(self):
        self.name = "voltron"
        self.health = 250
        self.power_level = 400
        self.weapon = "sword"
        self.attack_power = random.randint(0, 50)


class Dinosaur:
    def __init__(self):
        self.type = "Metal-Greymon"
        self.health = 150
        self.energy = 500
        self.attack_power = random.randint(0, 100)


# class Fleet:
#     def __init__(self):
#         self.robots = list()
#         self.robots.append(Robot())
#         self.robots.append(Robot())
#         self.robots.append(Robot())
#
#     # this function loops through health
#     def defeated(self):
#         for robot in self.robots:
#             if robot.health > 0:
#                 return False
#         return True
#
#
# class Herd:
#     def __init__(self):
#         self.dinosaurs = list()
#         self.dinosaurs.append(Dinosaur())
#         self.dinosaurs.append(Dinosaur())
#         self.dinosaurs.append(Dinosaur())
#
#     def defeated(self):
#         for dino in self.dinosaurs:
#             if dino.health > 0:
#                 return False
#         return True


# class Weapon:
#     def __init__(self):
#         self.weapon_1 = "sword"
#         self.weapon_2 = "axe"
#         self.weapon_3 = "pulse rifle"
#
#     def choose_weapon(self, player_choice=None):
#
#         if player_choice == "sword":
#             player = Robot()
#         elif player_choice == "axe":
#             player = Robot()
#         elif player_choice == "pulse rifle":
#             player = Robot()
#         return player
#
#     player_choice = input("Choose your weapon: sword, axe, pulse rifle")
#
#
# class dinoAttack:
#     def __init__(self):
#         self.attack1 = "giga storm"
#         self.attack2 = "mega claw"
#         self.attack3 = "metal arm"
#
#     def choose_attack(self, player_choice=""):
#         if player_choice == "giga storm":
#             player = Robot()
#         elif player_choice == "mega claw":
#             player = Robot()
#         elif player_choice == "metal arm":
#             player = Robot()
#         return player
#
#     player_choice = input("Choose your attack: giga storm, mega claw, metal arm")




# class Battlefield:

# this function loops through the fight sequence


# def fight_sequence():
#     robotOne = Fleet()
#     dinosaurOne = Herd()
#     turn = 'Dinosaur'
#     while not robotOne.defeated() and not dinosaurOne.defeated():
#         if turn == 'Dinosaur':
#             for robot in robotOne.robots:
#                 robot.health -= dinosaurOne.dinosaurs[0].attack_power
#             turn = 'Robot'
#         elif turn == 'Robot':
#             for dinosaur in dinosaurOne.dinosaurs:
#                 dinosaur.health -= robotOne.robots[0].attack_power
#             turn = 'Dinosaur'
#     print("The dinosaurs won: ", robotOne.defeated())
#     print("The robots won: ", dinosaurOne.defeated())
#
#
# fight_sequence()
