def sum_n(n):
	if n == 0:
		return 0
	small_n = sum_n(n-1)
	new = small_n+n
	return  new
n = int(input())
print(sum_n(n))