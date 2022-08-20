import threading     # I will be using a separate thread to allow the existance of more than 1 longcat if I choose to change the python script in the future.
                     
import time          # Used for python's time.sleep()
import random        # Used to spawn the longcat at a random location

from tkinter import Tk, Canvas, PhotoImage, NW # TK will be the UI toolkit i'll be using

def catThread(root): # this will be the thread used to organize the movement of the longcat

    # Set our original X/Y COORDS and X/Y Momentum to place and move the longcat per tick
    catPosX = random.randint(0, root.winfo_screenwidth()  - 300) # 300 is the hardcoded width of img
    catPosY = random.randint(0, root.winfo_screenheight() - 550) # 550 is the hardcoded height of img
    catMomX = 6 # chosen momentum for X/Y to my personal taste
    catMomY = 6
    
    while(1):
        # return and throw back the coords and momentum of the longcat
        catPosX, catPosY, catMomX, catMomY = makecatMove(root, catPosX, catPosY, catMomX, catMomY)
        #print("moving cat...")
        time.sleep(0.015) #sleep

def makecatMove(root, catPosX, catPosY, catMomX, catMomY):
    # keep a var for the farthest spaces our longcat can travel
    max_screen_width  = root.winfo_screenwidth()  - 300
    max_screen_height = root.winfo_screenheight() - 550

    # check if we are at an extreme pixel for left and right bounds, if so, reverse X momentum to bounce off
    if(catPosX >= max_screen_width or catPosX < 0 ):
        catMomX = catMomX * -1

    # always carry momentum no matter what
    catPosX = catPosX + catMomX

    # same as X momentim but for top and bottom bounds
    if(catPosY >= max_screen_height or catPosY < 0):
        catMomY = catMomY * -1
        
    catPosY = catPosY + catMomY

    # set geometry
    root.geometry("+" + str(catPosX) + "+" + str(catPosY))

    #return updated vals to be used next tick
    return catPosX, catPosY, catMomX, catMomY

# universal TK setup and mainloop
root = Tk()
root.attributes('-transparentcolor','#f0f0f0') #invis bg
root.attributes("-topmost", True) # attr to always move in front of windows

canvas = Canvas(root, width=300, height=550) # set to image width and height
canvas.pack() #commit canvas to window

img = PhotoImage(file="./longcat.png") # read img

canvas.create_image(0, 0, anchor=NW, image=img) # index img

root.overrideredirect(1) # needed for wanted visual behaviour

catPosThread = threading.Thread(target=catThread, args=(root,)) # start thread as described above
catPosThread.start()


root.mainloop()
