import os
from PIL import Image
items = os.listdir(".")

newlist = []
for names in items:
    if names.endswith(".png"):
        newlist.append(names)
        image = Image.open(names)
        image.show()
    if names.endswith(".jpg"):
        newlist.append(names)
        image = Image.open(names)
        image.show()
    if names.endswith(".jpeg"):
        newlist.append(names)
        image = Image.open(names)
        image.show()
 #   choice = input("Would you like to continue? (Y or N)")
#    choice.lower()

    #while (names != " "):
    #if (choice == "y"):
 #       continue
    #else:
 #       break
    
print (newlist)
