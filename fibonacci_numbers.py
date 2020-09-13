max = 1000
f = [0] * max

def fibo(n):
	if n == 0:
		return 0
	f_ant = 1
	f_atu = 1
	for i in range(2,n):
		f_prox = f_atu + f_ant
		f_ant = f_atu
		f_atu = f_prox
	return f_atu


def main(args):
	l=[]
	fim = False
	while not fim: 
		try:
			n=int(input())
			if type(n) == int:
				l.append(n)
		except:
			for i in range(len(l)):
				print(fibo(l[i]))
			break
			l=[]
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


  

