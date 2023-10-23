from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        # Top title
        title=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="Brown")
        title.place(x=0,y=0,width=1530,height=45)
        
        # Top image
        img_top1=Image.open(r"images_interface\dev2.jpeg")
        img_top1=img_top1.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=350)

        #  # image inside main_frame
        # img_f=Image.open(r"images_interface\dev2.jpeg")
        # img_f=img_f.resize((1530,720),Image.ANTIALIAS)
        # self.photoimg_f=ImageTk.PhotoImage(img_f)

        # f_lbl=Label(main_frame,image=self.photoimg_f)
        # f_lbl.place(x=300,y=0,width=200,height=200)

        # developer info

        dev_label = Label(main_frame,text=" 1) Somesh Gajanan Chincholkar",font=("times new roman",15,"bold"),bg="Violet")
        dev_label.place(x=0,y=30)

        dev_label = Label(main_frame,text=" 2) Yash Ramesh Ghyar",font=("times new roman",15,"bold"),bg="green")
        dev_label.place(x=0,y=90)

        dev_label = Label(main_frame,text=" 3) Aditya chopde",font=("times new roman",15,"bold"),bg="blue")
        dev_label.place(x=0,y=150)

        dev_label = Label(main_frame,text=" 4) Rohan Jorwar ",font=("times new roman",15,"bold"),bg="red")
        dev_label.place(x=0,y=210)

        dev_label = Label(main_frame,text=" 5) Rushikesh Merat ",font=("times new roman",15,"bold"),bg="Brown")
        dev_label.place(x=0,y=270)






if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()