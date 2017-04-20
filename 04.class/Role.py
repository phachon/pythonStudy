class Role(object):
	def __init__(self, name, role, weapon, life_value):
		self.name = name
		self.role = role
		self.weapon = weapon
		self.life_val = life_value


	def buy_weapon(self, weapon):
		print("%s is buying [%s]" %(self.name, weapon))

pl = Role("SanJiang", 'Police', 'B10', 90)
pl = Role("ChunYun", 'Police', 'B10', 11)
