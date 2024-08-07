#write a program to remove a duplicates in a list

numbers = [1, 1, 2 , 3 , 4 ,5]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


