fruits = ["apple", "raspberry", "pineapple", "cherry"]

if "apple" in fruits:
    print("Apple found at index:", fruits.index("apple"))

fruits[1:3] = ["orange"]
print("After replacing:", fruits)

fruits.insert(2, "apricot")
print("After inserting apricot:", fruits)


fruits.extend(["car", "bike", "aeroplane"])
print("Final list:", fruits)
