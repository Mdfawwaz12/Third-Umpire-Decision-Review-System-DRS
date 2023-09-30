import tkinter
import cv2
import PIL.Image,PIL.ImageTk #pil- python image library
#imageTk- tkinter to show images
from functools import partial
import threading #for tkinter mainloop runs compulsory, so using of thread
import imutils 
import time


Width = 762 # width and Height of main Screen
Height= 500

var2 = cv2.VideoCapture('video.mp4')
def play(speed):
    print(f"you click on fast, speed is {speed}")
    frame = var2.get(cv2.CAP_PROP_POS_FRAMES)
    var2.set(cv2.CAP_PROP_POS_FRAMES,frame + speed)

    grabbed, frame = var2.read() 
    if not grabbed: 
        exit()
    frame = imutils.resize(frame,width=Width,height=Height)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canva.image = frame
    canva.create_image(0,0,image=frame,anchor=tkinter.NW)


def pending(decision):
    if decision == 'out':
        var_condition = 'out.jpg'
    else:
        var_condition = 'Not out.jpg'
    #1.display decision image
    img = cv2.cvtColor(cv2.imread("Decision pending.jpg"),cv2.COLOR_BGR2RGB)
    img = imutils.resize(img, width=Width,height=Height)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    canva.image = img
    canva.create_image(0,0, image=img, anchor=tkinter.NW)
    #2.wait for 1 second
    time.sleep(1)
    #3.display out/not out image
    img = cv2.cvtColor(cv2.imread(var_condition),cv2.COLOR_BGR2RGB)
    img = imutils.resize(img, width=Width,height=Height)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    canva.image = img
    canva.create_image(0,0, image=img, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",)) #args-tuple,args - pending functions argument
    thread.daemon = 1
    thread.start()
    print("out")

def Not_out():
    thread = threading.Thread(target=pending, args=("Not Out",)) #args-tuple
    thread.daemon = 1
    thread.start()
    print("Not out")

var = tkinter.Tk()
var.title("Third Umpire ")
var.title("Third Umpire Decision Review System")

cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB) #image insertion

canva = tkinter.Canvas(var,width=Width, height=Height) 

pic = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img)) 

image_on_canvas = canva.create_image(0,0,ancho= tkinter.NW, image=pic)
canva.pack()

#buttons to control
btn = tkinter.Button(var, text="previous (fast)",width=40, command=partial(play, -20))
btn.pack()

btn = tkinter.Button(var, text="previous (slow)",width=40, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(var, text="Next (slow)",width=40, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(var, text="Next (fast)",width=40, command=partial(play, 20)) # command katho func ka name liknaso
btn.pack()
btn = tkinter.Button(var, text="Out",width=40,command=out)
btn.pack()

btn = tkinter.Button(var, text="Not Out",width=40,command=Not_out)
btn.pack()
var.mainloop()
