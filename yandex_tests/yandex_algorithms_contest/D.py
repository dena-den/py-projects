def generate(cur, op, cl, n):
	if len(cur) == 2*n:
		print(cur)
	if op < n:
		generate(cur + '(', op + 1, cl, n)
	if cl < op:
		generate(cur + ')', op, cl + 1, n)
	
def res(n):
	generate('', 0, 0, n)

n = int(input())
res(n)