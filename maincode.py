from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime








class maincode:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Top title
        title=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1530,height=45)

        # Top image
        img_top1=Image.open(r"images_interface\16.webp")
        img_top1=img_top1.resize((1520,740),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=45,width=1520,height=740)

        # button
        b1=Button(self.root,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1.place(x=555,y=705,width=400,height=60)

    # 2)
    # ****** attendance ******
    def mark_attendance(self,n,r,d):
        with open("attend.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))   
                name_list.append(entry[0])
            if((n not in name_list)) and ((r not in name_list)) and ((d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{d},{dtstring},{d1},present")





    
    # ********* Face Recognition ********

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="8771",database="newdb",port=3306)
                mycursor=conn.cursor()

                mycursor.execute("select Name from student where student_id="+str(id))
                n=mycursor.fetchone()
                n = "+".join(n)

                mycursor.execute("select Roll from student where student_id="+str(id))
                r = mycursor.fetchone()
                r = "+".join(r)

                mycursor.execute("select Dep from student where student_id="+str(id))
                d = mycursor.fetchone()
                d = "+".join(d)

                

                if confidence>77:
                    cv2.putText(img,f"Roll:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,y]

            return coord
    
        def recognize(img,clf,faceCascade):
            coord =draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    



if __name__ == "__main__":
    root = Tk()
    obj = maincode(root)
    root.mainloop()