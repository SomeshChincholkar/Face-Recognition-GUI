from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        # Top title
        title=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title.place(x=0,y=0,width=1530,height=45)
        
        # Top image
        img_top1=Image.open(r"images_interface\help4.webp")
        img_top1=img_top1.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label = Label(f_lbl,text="gmail: somesh.222104062@viit.ac.in",font=("times new roman",15,"bold"),bg="Violet")
        dev_label.place(x=550,y=220)

        dev_label = Label(f_lbl,text="Contact No. 1234567891",font=("times new roman",15,"bold"),bg="Violet")
        dev_label.place(x=550,y=260)

        





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()