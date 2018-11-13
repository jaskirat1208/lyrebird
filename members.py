class Members(object):
	"""docstring for Members"""
	def __init__(self,family,partners):
		self.family = family
		self.partners = partners

	def __str__(self):
		return str(self.family) + " " + str(self.partners)