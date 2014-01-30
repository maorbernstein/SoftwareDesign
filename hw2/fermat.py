def check_fermat(a,b,c,n):
    if (n>2):
	if (a**n + b**n == c**n):
        	print 'Holy smokes, Fermat was wrong!'
	else:
        	print "No that doesn't work."
    else:
        print "Don't cheat!"

def fermat():
    print 'Enter the four numbers neccessary for a fermat test.'
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    n = input('Enter n: ')
    check_fermat(int(a),int(b),int(c),int(n))

fermat()
