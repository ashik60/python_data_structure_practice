#Write a Python program to get the largest number from a list.

list = [2,4,6,8,1,100, 150, 20,23,45,21]

max= list[0]

for i in list:
    if i>max:
        max=i

print('Largest number of the list', max)