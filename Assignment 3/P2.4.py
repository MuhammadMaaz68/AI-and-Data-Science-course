scores = [40, 89, 90, 89, 23, 90, 50]

score= []

for item in scores:
    if item not in score:
        score.append(item)

score.sort(reverse=True)

first_best = score[0]
second_best = score[1]

print("First best score:", first_best)
print("Second best score:", second_best)
