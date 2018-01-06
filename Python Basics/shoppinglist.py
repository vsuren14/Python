# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:21:55 2018
Program to remainder the shppinglist
@author: suren
"""
print("Shopping cart")
def show_help():
    print("""
    Enter the shopping list one by one, give done once completed
    Enter show to ist the items in cart
    Enter help to show the items in cart """)
    
def show_items():
    print ("Items are")
    for item in shoppinglist:
        print(item)

def addtolist():
    shoppinglist.append(newitem)
    print("Item {} has been added to list, now we have {} items in list".format(newitem,len(
            shoppinglist)))
    
shoppinglist=[]
while True:
    newitem=input("Enter the items: ")
    if newitem == "done":
        break
    elif newitem == "help":
        show_help()
        continue
    elif newitem == "show":
        show_items()
        continue
    else:
        addtolist()
show_items()
