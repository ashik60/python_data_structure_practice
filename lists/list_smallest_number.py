# Write a Python program to get the smallest number from a list.

list = [2,4,6,8,1,100, 150, 20,23,45,21]

min= list[0]

for i in list:
    if i<min:
        min=i

print('Smallest number of the list', min)