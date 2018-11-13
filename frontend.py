import members as mb

def main():
	# x = int(input())
	m = raw_input().split(',')
	n = int(input())
	partners = {}
	for i in xrange(0,n):
		l = raw_input().split(',')
		partners[l[0]] = l[1]
		partners[l[1]] = l[0]
	fam = mb.Members(m,partners)
	print fam
	# for m in members:
		# add a member to the members list

if __name__ == '__main__':
	main()