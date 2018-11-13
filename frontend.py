import members as mb
import random
from timeit import default_timer as timer
from helper import *


algo = 1

def startsimulation(family,ls):
	for i in xrange(0,len(ls)):
		if family.ispartnerof(ls,i) :
			return 1

	return 0



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



	

def main():
	# x = int(input())
	# print fam
	fam = registration()
	ti = timer()
	ans = simulategifts(fam,algo)
	tf = timer()
	fam.print_pretty(ans)
	# print 'Time elapsed: ',(tf-ti)
	# for m in members:
		# add a member to the members list

if __name__ == '__main__':
	main()