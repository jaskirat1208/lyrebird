from timeit import default_timer as timer
from helper import *
import sys


algoused = 1


def main():
	fam = registration()
	n = sys.argv[1]
	print n
	# # n = input("Times to simulate")
	tot = 0
	algoused = 1
	for i in xrange(0,int(n)):
		# print "simulating for i =",i
		ti = timer()
		ans = simulategifts(fam,algoused)
		tf = timer()
		tot += tf-ti

	print "Cumulative switch time", str(tot/float(n))

	algoused = 2
	for i in xrange(0,int(n)):
		# print "simulating for i =",i
		ti = timer()
		ans = simulategifts(fam,algoused)
		tf = timer()
		tot += tf-ti
	print "Brute force select time", str(tot/float(n))




if __name__ == '__main__':
	main()