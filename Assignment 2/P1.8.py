num=int(input("Enter a number: "))

check = num in range(20,40,1)

if check:
    print("Number b/w 20-40")
else:
    print("Number not in range")
