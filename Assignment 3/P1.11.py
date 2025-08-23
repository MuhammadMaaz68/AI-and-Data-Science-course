def fac(n):
    if n < 0:
        return 1
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)

n = 5
fact = fac(n)
print(f"Factorial of {n} = {fact}")
