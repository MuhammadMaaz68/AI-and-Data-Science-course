nums = [32, 54, 66, 11, 77, 10, 90]
num=[]

for item in nums:
    if item>20:
        num.append(item)

print("After removing <20:", num)

num.sort()
print("Ascending:", num)
num.sort(reverse=True)
print("Descending:", num)

add=0
x=0
for items in num:
    add+=items
    x+=1

average=add/x
print("Average:", average)
