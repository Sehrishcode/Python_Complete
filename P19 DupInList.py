numbers = [2,2,4,6,6,3,1,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)