from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Top title
        title=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title.place(x=0,y=0,width=1530,height=45)
        
        # Top image
        img_top1=Image.open(r"images_interface\11.jpg")
        img_top1=img_top1.resize((765,325),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=55,width=765,height=325)

        img_top2=Image.open(r"images_interface\5.jpg")
        img_top2=img_top2.resize((765,325),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=765,y=55,width=765,height=325)

        # button betn topimages and bottomimage
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1.place(x=0,y=380,width=1530,height=60)

        # Bottom image
        img_bottom=Image.open(r"images_interface\4.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325) 

    def train_classifier(self):
        data_dir = ("Data_img")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]        # List Comprehension

        faces =[]
        ids = []

        for image in path:
            img = Image.open(image).convert('L')          
            imageNp = np.array(img,'uint8')                
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)


        # **** Train the classifier and save ****

        clf = cv2.face.LBPHFaceRecognizer_create()                                                                                                     # if LBPH... is not working or cv2 has no attribute occur then pip install opencv-contrib-python run in cmd
        clf.train(faces,ids)
        clf.write("clf.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Completed")



        
    






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()