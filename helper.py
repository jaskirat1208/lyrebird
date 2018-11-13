import members as mb
import random



def poprandom(ls):
	tem = random.randint(0,len(ls)-1)
	ans = ls[tem]
	ls.pop(tem)
	return ans

def registration():
	m = raw_input().split(',')
	n = int(input())
	partners = {}
	for i in xrange(0,n):
		l = raw_input().split(',')
		partners[l[0]] = l[1]
		partners[l[1]] = l[0]
	return mb.Members(m,partners)
