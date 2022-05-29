from tkinter import *
import shutil
import time
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2
from subprocess import call


def callTrainer():
    call(["python", "trainer.py"])


if __name__ == "__main__":
   root = Tk()
   root.geometry('1980x1080')
   root.configure(bg="#180020")
   root.minsize(1300,720)
   root.state("zoomed")
   root.title("Talaash")

image1=Image.open("bgImages/bg7.webp")
image1 = image1.resize((1700,980), Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(image1)
photo_label1=Label(image=photo1).place(x=0, y = 0)
photo_label1



Fullname=StringVar()
Fathername=StringVar()
Mothername=StringVar()
Bodymark=StringVar()
gen = IntVar()
Address = StringVar()
ContactNumber = StringVar()
rel=StringVar()
file1=""


image=Image.open("images.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=500,height=500).place(x=833,y=140)
photo_label

def ask():
   value=tmsg.askquestion("WARNING !","Select all (*) mandatory fields.\n(name,contact number, address,picture)\n\n If done already, then proceed. \n\n Will you like to proceed ?")
   if value=="yes":
      x=databaseEnter()
      if(x==1):
         tmsg.showinfo("Success","New Face Recorded Successfully")
         root.destroy()
      else:
         tmsg.showinfo("Warning","Please enter all (*) marked details")



def getid():
   conn = sqlite3.connect('missing.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('''select MAX(ROWID) from People''')
   conn.commit()
   for row in cursor:
    for elem in row:
        x = elem
   return x

def databaseEnter():

   name=Fullname.get()
   father=Fathername.get()
   mother=Mothername.get()

   body=Bodymark.get()
   address = Address.get()
   number = ContactNumber.get()

   gen1=""
   gender=gen.get()
   if(gender==1):
      gen1='Male'
   if(gender==2):
      gen1='Female'
   religion=rel.get()
   if(religion=="Select Religion"):
      religion=None

   if(name!="" and address != ""):
      conn = sqlite3.connect('missing.db')
      with conn:
         cursor=conn.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS People
                    (Name text, Gender text, Father text, Mother text, Religion text, Address text, ContactNumber text, Bodymark text)
                    ''')

      cursor.execute('''INSERT INTO People (Name,Gender,Father,Mother,Religion,Address, ContactNumber, Bodymark) VALUES (?,?,?,?,?,?,?,?)''',(name,gen1,father,mother,religion,address, number, body))
      conn.commit()
      x = getid()
      file="images/user." + str(x) + ".png"
      newPath = shutil.copy('temp/1.png',file)
   else:
      return 0
   return 1


def mfileopen():
   file1=filedialog.askopenfilename()
   print(file1)
   newPath = shutil.copy(file1, 'temp/1.png')
   image=Image.open('temp/1.png')
   image = image.resize((500,500), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(image)
   photo_label=Label(image=photo,width=500,height=500).place(x=833,y=140).pack()
   label_ = Label(root, text=file1,width=70,font=("bold", 8))
   label_.place(x=260,y=630)


label_0 = Label(root, text="Report a Missing Person",width=35,font=("Gill Sans Ultra Bold", 25),bg="#000000",fg='white')
label_0.place(x=360,y=80)

##################  form begin  ######################

frame = Frame(root, bg = "white")
frame.place(x = 130, y = 141, width = 701, height = 502)

label_1 = Label(frame, text="Name      *",width=20,font=("bold", 13), fg = "black").place(x=30,y=27)
entry_1 = Entry(frame,width=50,textvar=Fullname).place(x=260,y=27)

##############

label_2 = Label(frame, text="Father Name",width=20,font=("bold", 13)).place(x=30,y=77)
entry_2 = Entry(frame,width=50,textvar=Fathername).place(x=260,y=77)

##############

label_3 = Label(frame, text="Gender",width=20,font=("bold", 12)).place(x=30,y=127)


Radiobutton(frame, text="Male",padx = 5, variable=gen, value=1).place(x=260,y=127)
Radiobutton(frame, text="Female",padx = 20, variable=gen, value=2).place(x=315,y=127)

##############

label_4 = Label(frame, text="Mother Name",width=20,font=("bold", 12)).place(x=30,y=177)
entry_4 = Entry(frame,width=50,textvar=Mothername).place(x=260,y=177)


##############

label_5 = Label(frame, text="Religion",width=20,font=("bold", 12)).place(x=30,y=227)

list1 = ['Hindu','Muslim','Buddhist','Christian','Sikh','Jain','Others'];

droplist=OptionMenu(frame,rel, *list1)
droplist.config(width=30)
rel.set('Select Religion')
droplist.place(x=260,y=227)

##########

label_6 = Label(frame, text="Address     *",width=20,font=("bold", 12)).place(x=30,y=277)
entry_6 = Entry(frame,width=50,textvar=Address).place(x=260,y=277)

##############

label_7 = Label(frame, text="Contact Number       *",width=20,font=("bold", 12)).place(x=30,y=327)
entry_7 = Entry(frame,width=50,textvar=ContactNumber).place(x=260,y=327)

##############

label_8 = Label(frame, text="Body Mark",width=20,font=("bold", 12)).place(x=30,y=377)
entry_8 = Entry(frame,width=50,textvar=Bodymark).place(x=260,y=377)

##############

label_9 = Label(frame, text="Face Image      *",width=20,font=("bold", 12)).place(x=30,y=427)

btn=Button(frame, text="Select",width=20,command=mfileopen).place(x=260,y=427)
Button(root, text='Register',width=13,font=("bold",12),bg='brown',height=2,fg='white',command=ask).place(x=1210,y=650)

root.mainloop()
