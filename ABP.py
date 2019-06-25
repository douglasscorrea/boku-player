import math

class ABP():
	def __init__(self):
		self.alpha = -math.inf
		self.beta = math.inf

	def get_alpha(self):
		return self.alpha

	def get_beta(self):
		return self.beta
	
	def set_alpha(self, alpha):
		self.beta = alpha
		
	def set_beta(self, beta):
		self.beta = beta