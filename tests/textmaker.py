import random

def listToString(ls):
	s = ''
	for i in xrange(0,len(ls)-1):
		s += str(ls[i]) + ','
	s += str(ls[len(ls)-1])
	return (s)


n = input()
l = list(xrange(1,n+1))
s1 = listToString(l)
s2 = list(l)
random.shuffle(s2)
# s2 = listToString(l)
print s1
k = random.randint(0,n)
# k = 3
print k/2
for i in xrange(0,k,2):
	print str(s2[i]) + ',' + str(s2[i+1])
