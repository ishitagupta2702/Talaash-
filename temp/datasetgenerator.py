import cv2
import sqlite3

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertOrUpdate(Id,Name,Address,ContactNumber):
    conn=sqlite3.connect("missing.db")
    cmd="Select * from People where ROWID =" +str(Id)
    cursor=conn.execute(cmd)
    isRecordExists=0
    for row in cursor:
        isRecordExists=1
    if(isRecordExists==1):
        cmd="Update People Set Name="+str(Name)+", Address="+str(Address)+", ContactNumber="+str(ContactNumber)+" where ROWID="+str(Id)
    else:
        cmd="Insert into People(Id,Name,Address,ContactNumber) values("+str(Id)+","+str(Name)+","+str(Address)+","+str(ContactNumber)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

Id=raw_input('enter ID ')
Name=raw_input('enter Name ')
Address=raw_input('enter address ')
ContactNumber=raw_input('enter contact number ')
insertOrUpdate(Id,Name,Address,ContactNumber)
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #incrementing sample number
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+str(Id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.waitKey(100)

    cv2.imshow('face',img)
    #wait for 100 miliseconds
    cv2.waitKey(1)
    # break if the sample number is morethan 20
    if(sampleNum>20):
        break
cam.release()
cv2.destroyAllWindows()
