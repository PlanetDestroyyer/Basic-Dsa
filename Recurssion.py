def fact(n):
	if n == 0:
		return  1 
	return n*fact(n-1)
def sum_n(n):
	if n== 0:
		return  1 
	s_out = sum_n(n-1)
	output = s_out+n
	return  output
n = int(input())
print(fact(n))
print(sum_n(n))
	