student = ["Tahir", 44, "AI and Data Science", True]


string=[]
integer=[]
boolean=[]

for item in student:
    if type(item) == str:
        string.append(item)
    elif type(item) == int:
        integer.append(item)
    elif type(item) == bool:
        boolean.append(item)

print("Strings:", string)
print("Numbers:", integer)
print("Booleans:", boolean)
