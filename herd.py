from robot_dino import Dinosaur


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
