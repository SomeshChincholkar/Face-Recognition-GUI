from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student         
import os
from train import Train
from maincode import maincode
from attendance import Attendance
from developer import developer
from help import Help
import tkinter as tk                                                                                                                                # only for exit messagebox
 


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
 
        #First Image
        img=Image.open(r"images_interface\4.jpg")
        img=img.resize((550,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=150)

        #Second Image
        img1=Image.open(r"images_interface\8.jpg")
        img1=img1.resize((550,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=150)

        #Third Image
        img2=Image.open(r"images_interface\6.jpg")
        img2=img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=150)


        # Background Image
        img3=Image.open(r"images_interface\7.jpg")
        img3=img3.resize((1540,640),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1540,height=710)

        title=Label(bg_img,text="FACE  RECOGNITION  ATTENDENCE SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title.place(x=0,y=0,width=1530,height=45)


        # All commands will given after importing all files in all buttons
        #student button
        img4=Image.open(r"images_interface\student_button.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect face button
        img5=Image.open(r"images_interface\face_det.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_maincode_data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_maincode_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        

        #Attendance face button
        img6=Image.open(r"images_interface\attendence.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",command = self.attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help face button
        img7=Image.open(r"images_interface\helpdesk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",command=self.help,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Train face button
        img8=Image.open(r"images_interface\traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos face button
        img9=Image.open(r"images_interface\photostudent.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        # Developer face button
        img10=Image.open(r"images_interface\developers.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        # Exit face button
        img11=Image.open(r"images_interface\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.exit,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",command=self.exit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    # After student.py (importing student)
    # ******* function button ******** 

    def student_details(self):
       self.new_window = Toplevel(self.root)
       self.app = Student(self.new_window)



    def open_img(self):
        os.startfile("Data_img")

    
    def train_data(self):
       self.new_window = Toplevel(self.root)
       self.app = Train(self.new_window)


    def face_maincode_data(self):
       self.new_window = Toplevel(self.root)
       self.app = maincode(self.new_window)


    def attendance(self):
       self.new_window = Toplevel(self.root)
       self.app = Attendance(self.new_window)


    def developer(self):
       self.new_window = Toplevel(self.root)
       self.app = developer(self.new_window)

    def help(self):
       self.new_window = Toplevel(self.root)
       self.app = Help(self.new_window)

    def exit(self):
       self.exit = tk.messagebox.askyesno("Face Recognition","Are you sure",parent=self.root)
       if self.exit >0:
          self.root.destroy()
       else:
          return
          


if __name__== "__main__":
    root=Tk()                     
    obj=Face_Recognition_System(root)    
    root.mainloop()
    

            
            


            
             
             