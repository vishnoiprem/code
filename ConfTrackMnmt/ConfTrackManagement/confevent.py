class ConfEvent:
	"""
	This class represents a talk and valuable info for each talk
	**__repr__: Return a string containing a printable representation of an object.
	**__init__: Method initilaise event name, event duration and scheduled informatoon
	"""
	def __init__(self,name,duration):
		self.name=name
		self.duration=duration
		self.scheduled=False
		#print('Event:__init__ :self.name : self.duration : self.scheduled: ', self.name, self.duration, self.scheduled)

	def __repr__(self):
		#print('Event:__repr__ :self.name : ',self.name)
		return self.name