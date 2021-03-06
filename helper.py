import members as mb
import random


def startsimulation(family,ls):
	for i in xrange(0,len(ls)):
		if family.ispartnerof(ls,i) :
			return 1

	return 0


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


def cumulativesim(family):
	familymembers = (family.family())
	ls = list(familymembers)
	random.shuffle(ls)
	ans = startsimulation(family,ls)
	while ans == 1:
		ls = list(family.family())
		random.shuffle(ls)
		ans = startsimulation(family,ls)			
	return ls


def simulateonebyone(family):
	ls = []
	flag = 1
	while flag:
		familymembers = family.family()
	# temp = family.family()
		restart = 0
		for f in familymembers:
			t = poprandom(familymembers)
			if family.partners(t,f) or t == f:
				# restart the simulation
				restart = 1
				break
			ls.append(t)
		if restart == 0:
			flag = 0

	return ls


def simulategifts(family,alg = 1):
	# familymembers = (family.family())
	if alg == 1:
		# print family
		return cumulativesim(family)
	elif alg == 2:
		#FOR EACH MEMBER, DRAW A RANDOM ITEM FROM THE LIST AND SIMULATE
		# print family
		return simulateonebyone(family)

