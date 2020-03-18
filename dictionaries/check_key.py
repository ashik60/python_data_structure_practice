#Write a Python script to check whether a given key already exists in a dictionary. 
y={'carl':40,'alan':2,'bob':1,'danny':3}

def key_present(x):
    if x in y:
        print('Key exists!')
    else:
        print("Key doesn't exist")

key_present('carl')
key_present('shayan')