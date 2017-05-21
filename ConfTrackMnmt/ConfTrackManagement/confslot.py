class ConfSlot:
	"""
	This class contains morning or evening slot information and validations
	for sessions
	"""
	def __init__(self,max_s,min_s=0):
		self.max=max_s
		self.min=min_s
		"""
		print min and max session for debug code
		"""
		#print('self.max',max_s)
		#print('self.min',min_s)

	def isValidEvent(self,event,totaltime):
		#print('Start 5: Slot:isValidEvent : event.duration,  self.max , event.duration+totaltime>self.max it will return False When condtion is True) :',event.duration,  self.max , event.duration+totaltime>self.max)
		
		"""
		Check weather event is valid or not 
		event time is more than 180 min or  combination of multiple evnets more than (180 or 240)  
		"""
		
		if event.duration>self.max or event.duration+totaltime>self.max:
			return False
		return True

	def isValidSession(self,totaltime):

		
		"""
		Check weather session is valid or not..
		if session time is more than 0 and total session time is less than 180 or 240 
		"""
		#print('Slot:isValidSession :self.min, self.max, totaltime', self.min,  self.max , totaltime)

		validsession=False
		if self.min:
			if totaltime>0 and totaltime<=self.max:
				validsession=True
		else:
			if totaltime==self.max:
				validsession=True 
		#print('end 5:Slot:isValidSession :self.min, self.max, totaltime', self.min,  self.max , totaltime)

		return validsession