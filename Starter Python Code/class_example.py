#################### Class ######################

class Taxi(object):
	"""docstring for Taxi"""
	def __init__(self, type):
		super(Taxi, self).__init__()
		if type == 'bus':
			self.max_passangers = 7
		else:
			self.max_passangers = 4



taxi1 = Taxi('Bus')


grid = [['X','X','X','X','X']\
       ,['X','X','X','X','X']]
#print taxi1.max_passangers

for i in grid:
	print i
