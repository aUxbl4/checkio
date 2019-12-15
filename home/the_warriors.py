# The Warriors
# https://py.checkio.org/en/mission/the-warriors/

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True
    # Check test Warrior
    #def info(self):
    #    print("War health {}. attack {}".format(self.health, self.attack))


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7
    # check test knight	
    #def info1(self):
    #    print(" King health {}. attack {}".format(self.health, self.attack))


def fight(unit_1, unit_2):
    unit_2.health -= unit_1.attack
    #unit_1.info()
    #unit_2.info()
    unit_22 = unit_1
    unit_11 = unit_2
    if unit_2.health > 0:
        fight(unit_11, unit_22)
    else:
        unit_2.is_alive = False
    return unit_1.is_alive
