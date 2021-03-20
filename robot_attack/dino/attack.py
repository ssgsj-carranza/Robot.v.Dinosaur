from robot_dino import Robot
from robot_dino import Dinosaur

class Weapon:
    def __init__(self):
        self.weapon_1 = "sword"
        self.weapon_2 = "axe"
        self.weapon_3 = "pulse rifle"

    def choose_weapon(self, player_choice=None):

        if player_choice == "sword":
            player = Robot()
        elif player_choice == "axe":
            player = Robot()
        elif player_choice == "pulse rifle":
            player = Robot()
        return player

    player_choice = input("Choose your weapon: sword, axe, pulse rifle")


class dinoAttack:
    def __init__(self):
        self.attack1 = "giga storm"
        self.attack2 = "mega claw"
        self.attack3 = "metal arm"

    def choose_attack(self, player_choice=""):
        if player_choice == "giga storm":
            player = Dinosaur()
        elif player_choice == "mega claw":
            player = Dinosaur()
        elif player_choice == "metal arm":
            player = Dinosaur()
        return player

    player_choice = input("Choose your attack: giga storm, mega claw, metal arm")