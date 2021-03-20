from herd import Herd
from fleet import Fleet


class BattleField:

    def fight_sequence(self):
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


BattleField().fight_sequence()
