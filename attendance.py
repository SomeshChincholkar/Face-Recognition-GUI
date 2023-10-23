from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # ***** Variabels ******        # after import and export csv

        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendence = StringVar()


        #First Image
        img=Image.open(r"images_interface\13.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #Second Image
        img1=Image.open(r"images_interface\15.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        # bg image
        img3=Image.open(r"images_interface\7.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title=Label(bg_img,text=" ATTENDENCE SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1530,height=45)

        m_frame = Frame(bg_img,bd=2,bg="white")
        m_frame.place(x=10,y=55,width=1520,height=600)
        
        # left label frame
        l_frame = LabelFrame(m_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font="SUNKEN 12 bold")
        l_frame.place(x=10,y=10,width=760,height=560)

        img_left=Image.open(r"images_interface\7.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(l_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame = Frame(l_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=720,height=370)



        # Labels and entry

        

        #Student Name
        student_name_label = Label(left_inside_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # Student Roll
        student_roll_label = Label(left_inside_frame,text="Roll.No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)


        #Department
        dep_label = Label(left_inside_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dep_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        dep_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("verdana",12,"bold"))
        dep_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_inside_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_inside_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_inside_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        self.attend_combo=ttk.Combobox(left_inside_frame,width=13,textvariable=self.var_atten_attendence,font=("verdana",12,"bold"),state="readonly")
        self.attend_combo["values"]=("Status","Present","Absent")
        self.attend_combo.current(0)
        self.attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=45)

        #Import button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        #Export button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # Right label frame
        r_frame = LabelFrame(m_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font="SUNKEN 12 bold")
        r_frame.place(x=780,y=10,width=720,height=560) 


        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(r_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=710,height=455)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("Name","Roll_No","Department","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        # self.attendanceReport.heading("ID",text="Attendance-ID")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")

        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        # self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)

        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)  # after making get_cursor fun.



   #  *********fetch data*******
        
    def fetchData(self,rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)


    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found",parent = self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                export_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)          
                messagebox.showinfo("Data Export","Data Export Sucessfully to "+ os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent = self.root)


    
    def get_cursor(self,event=""):
        cursor_row = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_row)
        rows = content['values']
        self.var_atten_name.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendence.set(rows[5])


    def reset_data(self):
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")






if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()