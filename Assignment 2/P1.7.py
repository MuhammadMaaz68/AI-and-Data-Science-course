num1=float(input("Enter num 1: "))
num2=float(input("Enter num 2: "))
sign = input("Enter the sign of what u want to perform +,-,*,/: ")

if num1 > num2 and sign == "/":
    print(num1/num2)
else:
    print("Div not possible due to numerator is smaller then denominator")

if sign == "*":
    print(num1*num2)
elif sign == "-":
    print(num1-num2)
elif sign == "+":
    print(num1+num2)
