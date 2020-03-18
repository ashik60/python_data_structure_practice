#1. Write a Python script to sort 
# (ascending and descending) a dictionary by value. 

y={'carl':40,'alan':2,'bob':1,'danny':3} 
l=list(y.items()) #convert into list
#print(l)
l.sort()    #ascending sort
y=dict(l)   #convert into dict
print(y)

l=list(y.items())
l.sort(reverse=True)    #descending sort
y= dict(l)
print(y)