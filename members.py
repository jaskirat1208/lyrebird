class Members(object):
	"""docstring for Members"""
	def __init__(self,family,partners):
		self.__family = family
		self.__partners = partners

	def family(self):
		return list(self.__family)

	def ispartnerof(self,ls,i):
		partner = self.__partners.get(self.__family[i],'-1')
		if partner == '-1':
			return 0 
		if (partner == ls[i]) or (self.__family[i] == ls[i]):
			return 1
		return 0

	def __str__(self):
		return str(self.__family) + " " + str(self.__partners)

	def partners(self,t,f):
		if self.__partners.get(t,-1) == f:
			return 1
		return 0
		
	def print_pretty(self,ls):
		for i in xrange(0,len(self.__family)):
			print self.__family[i] + ' gives his gift to ' + ls[i]