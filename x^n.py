def solve(n):
	if n == 0:
		return 1
	small_n = solve(n-1)
	out = small_n*x
	return  out
x = int(input())
n = int(input())
print(solve(n))