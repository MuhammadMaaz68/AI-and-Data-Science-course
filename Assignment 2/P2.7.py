i=int(input("Enter a number: "))
fac=1
x=1

while True:
    if x<=i:
        fac*=x
        x+=1
    else:
        print(f"Factorial of {i} = {fac}")
        break
