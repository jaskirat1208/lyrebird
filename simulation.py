from frontend import *
from timeit import default_timer as timer
import sys

algo1 = 2


def main():
	fam = registration()
	n = sys.argv[1]
	print n
	# # n = input("Times to simulate")
	tot = 0
	for i in xrange(0,int(n)):
		print "simulating for i =",i
		ti = timer()
		ans = simulategifts(fam,algo1)
		tf = timer()
		tot += tf-ti
	print tot/float(n)


if __name__ == '__main__':
	main()