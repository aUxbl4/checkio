class Warrior:
	def __init__(self):
		self.health = 50
		self.attack = 5
		self.is_alive = True

	def info(self):
		print("War health {}. attack {}".format(self.health, self.attack)) 

class Knight(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 7
	
	def info1(self):
		print(" King health {}. attack {}".format(self.health, self.attack)) 
	

def fight(unit_1, unit_2):
	i = 0
	while unit_1.health > 0 and unit_2.health > 0:
		i += 1
		print(' HOD - ', i)
		if unit_1.health > 0:
			unit_2.health -= unit_1.attack
			unit_2.info()
		else:
			unit_1.is_alive = False
			break
		if unit_2.health > 0:
			unit_1.health -= unit_2.attack 
			unit_1.info()
		else:
			unit_2.is_alive = False
			break
	return unit_1.is_alive

tree_111 = Warrior()
tree_11.info()
tree_1.is_alive

tree_222 = Warrior()


tree_2 = Knight()
tree_221.info()
tree_2.is_alive


fight(tree_111,tree_222)
