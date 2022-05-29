from tkinter import *
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from tkinter.font import Font
from tkinter import ttk
from subprocess import call


def register():
    call(["python", "register.py"])
def liveSurveillance():
    call(["python", "surveillance.py"])
def detectPerson():
    call(["python", "detect.py"])
def videoSurveillance():
    call(["python", "videoSurveillance.py"])


root = Tk()
root.geometry('1500x1000')


root.title("Talaash")


image1 = Image.open("talaash1.png")
image1 = image1.resize((1500,200), Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(image1)
photo_label1=Label(image=photo1,width=1500,height=200).place(x=0,y=0)
photo_label1


image = Image.open("homepage.jpg")
image = image.resize((1500, 750), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=1500,height=750).place(x=0,y=165)
photo_label


Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""

#Gill Sans Ultra Bold


label_0 = Label(root, text="with you,",width=7,font=("Baskerville Old Face", 60),bg="#000000",fg="white").place(x = 40, y = 312) #112
label_next = Label(root, text="every step of the way.",width=16,font=("Baskerville Old Face", 40),bg="#000000",fg="white").place(x = 40, y = 396) #196

Button(root, text='REPORT A MISSING PERSON   >',width=30,height=2,bg='#EE3A8C',fg='white', activebackground='#FF69B4', font=("Lucida Sans", 12),command=register).place(x=188,y=680)
Button(root, text='PHOTO MATCH   >',width=25,height=2,bg='#EE3A8C',fg='white',activebackground='#FF69B4', font=("Lucida Sans", 12),command=detectPerson).place(x=510,y=680)
Button(root, text='LIVE SURVEILLANCE   >',width=25,height=2,bg='#EE3A8C',fg='white', activebackground='#FF69B4', font=("Lucida Sans", 12),command=liveSurveillance).place(x=795,y=680)
Button(root, text='VIDEO SURVEILLANCE   >',width=25,height=2,bg='#EE3A8C',fg='white', activebackground='#FF69B4', font=("Lucida Sans", 12),command=videoSurveillance).place(x=1080,y=680)

root.mainloop()
