gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

strings=[]
numbers=[]
for item in gadgets:
    if type(item) == str:
        strings.append(item)
    elif type(item) == int or type(item) == float:
        numbers.append(item)

print("Strings:", strings)
print("Numbers:", numbers)

strings.sort()
print("Strings ascending:", strings)
strings.sort(reverse=True)
print("Strings descending:", strings)


strings= sorted(strings, key=len)
print("Strings by length:", strings)

numbers.sort()
print("Numbers ascending:", numbers)
numbers.sort(reverse=True)
print("Numbers descending:", numbers)

