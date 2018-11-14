import members as mb
import random
from timeit import default_timer as timer
from helper import *


algo = 1


	

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