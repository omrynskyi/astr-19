class animal:
	def __init__(self, len_arm, len_leg, num_eye, tail,furry):
		self.len_arm = len_arm
		self.len_leg = len_leg	
		self.num_eye = num_eye
		self.tail = tail
		self.furry = furry

	def __str__(self):
	    return f"length of arm: {self.len_arm}\nlength of leg: {self.len_leg}\nnumber of eyes: {self.num_eye}\n{'has tail' if self.tail else 'no tail'}\n{'is furry' if self.furry else 'not furry'}"


animal1 = animal(30.2,43.7,6,True,True)
print(animal1)