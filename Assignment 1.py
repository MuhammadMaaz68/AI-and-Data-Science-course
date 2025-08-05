a = 15
b = 4

print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponentiation: a ** b =", a ** b)




x = 10
print("Initial value of x:", x)

x += 5
print("After x += 5:", x)

x *= 2
print("After x *= 2:", x)

x -= 4
print("After x -= 4:", x)

x /= 2
print("After x /= 2:", x)




a = 7
b = 10

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)







x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


# A bit of error in code only institute is defined not my_var so i changed all to my_var

my_var= "Saylani Mass IT"

print("’s’ in institute:", "s" in my_var)
print("'Saylani' in institute:", "Mass" in my_var)
print("'Saylani' not in institute:", "Saylani" not in my_var)




a = 5
b = 5
c = 1000

print("a is b:", a is b)
print("a is c:", a is c)
print("c is not b:", c is not b)



#Bonus Challenge:

#Write a mini program that:
#- Take user name and password as input.
#- You have to compare the user name with “Talha” and password with “Axiom123”.
#- How can we write this comparison in Python (provide syntax)


user = "Talha"
passw = "Axiom123"

userInput = input("Input your username: ")
passInput = input("Input your password: ")

check= (user == userInput and passw == passInput)

print("Username and/or Password are : ", check)
