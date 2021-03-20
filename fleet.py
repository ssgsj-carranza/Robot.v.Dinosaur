from robot_dino import Robot


class Fleet:
    def __init__(self):
        self.robots = list()
        self.robots.append(Robot())
        self.robots.append(Robot())
        self.robots.append(Robot())

    # this function loops through health
    def defeated(self):
        for robot in self.robots:
            if robot.health > 0:
                return False
        return True