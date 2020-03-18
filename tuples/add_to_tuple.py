#5. Write a Python program to add an item in a tuple.
t=(12,56,"Shaheen")
t=t+(5,) #using merge of tuples with the + operator
print(t)

t=t[:2]+(10,20,30)+t[2:]    #adding items in a specific index
print(t)

#use different ways to add items in list
li= list(t)
li.append(56)
t=tuple(li)
print(t)