num = int(input("Enter a number: "))
is_Prime= True
if num <= 1:
    is_Prime = False

elif num == 2:
    is_Prime = True

if num%2 ==0:
    is_Prime = False

i = 3
while i*i < num:
    if num%i ==0:
        is_Prime = False
    else:
        is_Prime = True
    i += 2

if is_Prime:
    print("Number is prime")

else:
    print("Number is Not Prime")
