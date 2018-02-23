#!/usr/bin/python3
import os
import glob
from PIL import Image

#image = Image.open('so cute.png')
#image.show()

for file in os.listdir("/Users/DesireeMora/Desktop/Education/Computer Concepts/Python/Voice-Namer"):
    if (file.endswith(".png")) or (file.endswith(".jpg") ) or (file.endswith(".jpeg")):
        print(os.path.join("/Users/DesireeMora/Desktop/Education/Computer Concepts/Python/Voice-Namer", file))


