from stegano import lsb
secretmessage=lsb.hide("FunnySheep.jpg","This is the hidden text inside the image")
secretmessage.save("NewFunnySheep.jpg")

