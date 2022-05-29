from tkinter import *
from tkinter import ttk
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2,os
import face_recognition as fr
import numpy as np
import math
import winsound

if __name__ == "__main__":
   root = Tk()
   root.geometry('1350x800')
   root.minsize(1350,800)
   root.configure(bg="#000000")
   root.state("zoomed")
   root.title("Talaash")

image1=Image.open("bgImages/bg1.jpg")
image1 = image1.resize((1300,800), Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(image1)
photo_label1=Label(image=photo1).place(x=70,y=0)
photo_label1


image2=Image.open("bgImages/facial-recognition.png")
image2 = image2.resize((500,500), Image.ANTIALIAS)
photo2=ImageTk.PhotoImage(image2)
photo_label2=Label(image=photo2,width=500,height=0).place(x=730,y=240)
photo_label2




image=Image.open("imageMissing.png")
# f = mp3play.load('Sound.mp3');
# play = lambda: f.play()
image = image.resize((400,400), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=400,height=400).place(x=60,y=200)
photo_label


label_1 = Label(root, text="Select a picture",bg='#000000',fg='#FCFCFC',width=30,font=("bold", 15))
label_1.place(x=83,y=170)
label_177 = Label(root, text="Double click on record to see details",bg='#000000',fg='#FCFCFC',width=50,font=("bold", 15))
label_177.place(x=740,y=102)

label_0 = Label(root, text = "PHOTO MATCH",  bg="#000000", fg="#FCFCFC", width = 60, font=("Gill Sans Ultra Bold", 30), anchor = CENTER)
label_0.place(x = 47, y = 39)

'''
def View():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tkinter.END, values=row)
    conn.close()
'''
####################################################################
# ###############  Get data ##########################################
# cascadePath = "haarcascade_frontalface_default.xml"
# faceDetect = cv2.CascadeClassifier(cascadePath)
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read("recognizer\\training_data.yml")

#################################################################3##
def viewdetail(a):
   conn = sqlite3.connect("missing.db")
   cur = conn.cursor()
   cur.execute("SELECT * FROM people where ROWID="+str(a))
   rows = cur.fetchall()
   print(rows)
   for row in rows:
      label_n = Label(root, text=row[0],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_n.place(x=1100,y=400)
      label_f = Label(root, text=row[2],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_f.place(x=1100,y=430)
      label_m = Label(root, text=row[3],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_m.place(x=1100,y=460)
      label_g = Label(root, text=row[1],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_g.place(x=1100,y=490)
      label_r = Label(root, text=row[4],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_r.place(x=1100,y=520)
      label_bl = Label(root, text=row[5],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_bl.place(x=1100,y=550)
      label_b = Label(root, text=row[6],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_b.place(x=1100,y=580)
      label_n = Label(root, text=row[7],bg="#000080",fg='white',width=20,font=("bold", 12))
      label_n.place(x=1100,y=610)


   # it print all records in the database
   conn.close()
   ################################################################################

   label_name = Label(root, text="Name",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_name.place(x=930,y=400)
   label_father = Label(root, text="FatherName",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_father.place(x=930,y=430)
   label_mother = Label(root, text="MotherName",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_mother.place(x=930,y=460)
   label_gender = Label(root, text="Gender",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_gender.place(x=930,y=490)
   label_religion = Label(root, text="Religion",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_religion.place(x=930,y=520)
   label_bloodgroup = Label(root, text="Address",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_bloodgroup.place(x=930,y=550)
   label_body = Label(root, text="Contact Number",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_body.place(x=930,y=580)
   label_nat = Label(root, text="BodyMark",bg="#191970",fg='white',width=20,font=("bold", 12))
   label_nat.place(x=930,y=610)

   #############################################################################


   #############################################################################
   x='user.'+str(a)+".png"
   image=Image.open('images/'+ x)
   image = image.resize((250,250), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(image)
   photo_l=Label(image=photo,width=250,height=250).place(x=690,y=400).pack()


def mfileopen():
   cleartree()
   file1=filedialog.askopenfilename()
   print(file1)
   newPath = shutil.copy(file1, 'temp/1.png')
   image=Image.open('temp/1.png')
   image = image.resize((400,400), Image.ANTIALIAS)
   photo=ImageTk.PhotoImage(image)
  # photolbl=Label(image=photo,width=400,height=400).place(x=90,y=110).pack()
   photolbl=Label(image=photo,width=400,height=400).place(x=60,y=200).pack()


def cleartree():
   records=tree.get_children()
   for el in records:
      tree.delete(el)


def doubleclick(event):
   item=tree.selection()
   itemid=tree.item(item,"values")
   ide=itemid[0]
   ide=(int(ide))
   viewdetail(ide)

def load_images_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
      images.append(filename)
    return images

def showPercentageMatch(face_distance,face_match_threshold=0.6):
    if face_distance > face_match_threshold:
      range = (1.0 - face_match_threshold)
      linear_val = (1.0 - face_distance) / (range * 2.0)
      return linear_val
    else:
      range = face_match_threshold
      linear_val = 1.0 - (face_distance / (range * 2.0))
      return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))


def View():
    cleartree()
    frame =cv2.imread("temp/1.png")
    #Resize the frame of video to 1/4 size for fast process
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

    #convert the image to BGR color(openCV) to RGB color(face_recognition)
    rgb_small_frame=small_frame[:,:,::-1]

    #Only process every other frame of video to save time
    if process_this_frame:
        #find all the faces and face encodings in the current frame of video
        face_locations=fr.face_locations(rgb_small_frame)
        face_encodings=fr.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
          #See if the face is a match for known face(s)
          matches=fr.compare_faces(encodings,face_encoding)
          print(matches)
          Id=0
          face_distances=fr.face_distance(encodings,face_encoding)
          best_match_index=np.argmin(face_distances)
          percent=showPercentageMatch(face_distances[best_match_index])

          if matches[best_match_index]:
            Id=known_face_names[best_match_index]
          face_names.append(Id)

          confidence=str(round(percent*100,2))+"%"

          conn = sqlite3.connect("missing.db")
          cur = conn.cursor()
          cur.execute("SELECT ROWID,Name,Address, ContactNumber FROM People where ROWID="+str(Id))
          rows = cur.fetchall()
          print(rows)

          if(len(rows)>0):
            row=rows[0]
            a="Matching "+str(percent*100)+"%"
            tree.insert("", 'end', values=row)
            tree.bind("<Double-1>",doubleclick)
            # play()
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


          else:
            a="No Match Found"


          label_Match = Label(root, text=a,bg="#000080",fg='yellow',width=35,font=("bold", 20))
          label_Match.place(x=20,y=710)

          conn.close()

Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""

btn=Button(text="Select photo",bg='#FFF68F',width=20, height = 1, command=mfileopen).place(x=165,y=620)

#== showing treeview
tree = ttk.Treeview(root, column=("column1", "column2", "column3","column4"), show='headings')
ttk.Style().configure("Treeview.Heading",font=('Calibri', 16,'bold'), foreground="black", relief="flat")

tree.heading("#1", text="Missing Person-ID")
tree.column("#1", minwidth=0, width=200, stretch=NO)

tree.heading("#2", text="Name")
tree.column("#2", minwidth=0, width=220, stretch=NO)

tree.heading("#3", text="Address")
tree.column("#3", minwidth=0, width=150, stretch=NO)

tree.heading("#4", text="Number")
tree.column("#4", minwidth=0, width=130, stretch=NO)

tree.place(x=630,y=130)


images=load_images_from_folder("images")

#get image names
images_name=[]
for img in images:
      images_name.append(fr.load_image_file(os.path.join("images",img)))

#get their encodings
encodings=[]
for img in images_name:
      encodings.append(fr.face_encodings(img)[0])


#get id from images
known_face_names=[]
for name in images:
      known_face_names.append((os.path.splitext(name)[0]).split('.')[1])


face_locations=[]
face_encodings=[]
face_names=[]
process_this_frame=True



b2=Button(text="View Matching Records",width=25,height=2,command=View,bg='#8B0000',fg="white").place(x=150,y=660)


root.mainloop()
