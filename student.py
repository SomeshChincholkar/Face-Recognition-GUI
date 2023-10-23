from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        # 3)
        # ***** variables *****
        # $
        for x in ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address"):
            exec(f"self.var_{x} = StringVar()")
            # exec is a built in function in python

        # 1)
        #First Image
        img=Image.open(r"images_interface\1.jpg")
        img=img.resize((550,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=150)

        #Second Image
        img1=Image.open(r"images_interface\students1.jpg")
        img1=img1.resize((550,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=150)

        #Third Image
        img2=Image.open(r"images_interface\students2.jpg")
        img2=img2.resize((550,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=150)

        # Background Image
        img3=Image.open(r"images_interface\7.jpg")
        img3=img3.resize((1560,640),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1560,height=710)

        title=Label(bg_img,text="STUDENTS INFORMATION ",font=("times new roman",35,"bold"),bg="red",fg="white")
        title.place(x=0,y=0,width=1530,height=45)

        m_frame = Frame(bg_img,bd=2,bg="white")
        m_frame.place(x=10,y=55,width=1500,height=600)

        # left label frame
        l_frame = LabelFrame(m_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font="SUNKEN 12 bold")
        l_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"images_interface\3.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(l_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # First frame
        # current course info
        cc_frame = LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font="SUNKEN 12 bold")
        cc_frame.place(x=5,y=135,width=720,height=200)

        # Department
        dep_label=Label(cc_frame,text="Department",font="SUNKEN 12 bold",bg = "skyblue")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font="SUNKEN 12 bold",width=17,state="read only") 
        dep_combo["values"]=("Select Department","comp","IT","Mech","AI")
        dep_combo.current(0)        # current position 0 = select dep.
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        # Course
        dep_label=Label(cc_frame,text="Course",font="SUNKEN 12 bold",bg = "skyblue")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_course,font="SUNKEN 12 bold",width=17,state="read only") 
        dep_combo["values"]=("Select Course","FY","SY","TY","FY")
        dep_combo.current(0)        
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        dep_label=Label(cc_frame,text="Year",font="SUNKEN 12 bold",bg = "skyblue")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font="SUNKEN 12 bold",width=17,state="read only") 
        dep_combo["values"]=("Select Year","2022-23","2023-24","2024-25")
        dep_combo.current(0)        
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # Semester
        dep_label=Label(cc_frame,text="Semester",font="SUNKEN 12 bold",bg = "skyblue")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_sem,font="SUNKEN 12 bold",width=17,state="read only") 
        dep_combo["values"]=("Select Semester","semester-1","semester-2")
        dep_combo.current(0)       
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Second frame
        # class student info. frame
        cs_frame = LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font="SUNKEN 12 bold")
        cs_frame.place(x=5,y=250,width=720,height=300)

        # student id label in cs_frame
        SID_label=Label(cs_frame,text="Student Id",font="SUNKEN 12 bold",bg = "skyblue")
        SID_label.grid(row=0,column=0,padx=10,sticky=W)

        SID_entry = ttk.Entry(cs_frame,textvariable=self.var_id,width=20,font="SUNKEN 12 bold")       
        SID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        # student name label in cs_frame
        SName_label=Label(cs_frame,text="student Name",font="SUNKEN 12 bold",bg = "skyblue")
        SName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        SID_entry = ttk.Entry(cs_frame,textvariable=self.var_name,width=20,font="SUNKEN 12 bold")       
        SID_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division label in cs_frame
        cd_label=Label(cs_frame,text="Class division",font="SUNKEN 12 bold",bg = "skyblue")
        cd_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        cd_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_div,font="SUNKEN 12 bold")       
        cd_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no. label in cs_frame
        rn_label=Label(cs_frame,text="Roll No.",font="SUNKEN 12 bold",bg = "skyblue")
        rn_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rn_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_roll,font="SUNKEN 12 bold")       
        rn_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # Gender in cs_frame
        gd_label=Label(cs_frame,text="Gender",font="SUNKEN 12 bold",bg = "skyblue")
        gd_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gd_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_gender,font="SUNKEN 12 bold")       
        gd_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        # We can also make combo box to gender male or female i.e entry or combo

        # DOB label in cs_frame
        rn_label=Label(cs_frame,text="DOB",font="SUNKEN 12 bold",bg = "skyblue")
        rn_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        rn_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_dob,font="SUNKEN 12 bold")       
        rn_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email in cs_frame
        em_label=Label(cs_frame,text="Email",font="SUNKEN 12 bold",bg = "skyblue")
        em_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        em_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_email,font="SUNKEN 12 bold")       
        em_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone no. in cs_frame
        pn_label=Label(cs_frame,text="Phone No.",font="SUNKEN 12 bold",bg = "skyblue")
        pn_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        pn_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_phone,font="SUNKEN 12 bold")       
        pn_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address in cs_frame
        ad_label=Label(cs_frame,text="Address",font="SUNKEN 12 bold",bg = "skyblue")
        ad_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        ad_entry = ttk.Entry(cs_frame,width=20,textvariable=self.var_address,font="SUNKEN 12 bold")       
        ad_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        b1 = ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")          # only variable in radiobutton not textvariable
        b1.grid(row=6,column=0)

        
        b2 = ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="No photo sample",value="No")          # data will store in only one variable
        b2.grid(row=6,column=1)

        # button frame
        b_frame = Frame(cs_frame,bd=2,relief=RIDGE,bg="white")
        b_frame.place(x=0,y=210,width=710,height=35)
        
        # buttons in button frame    
        save_b = Button(b_frame,text="Save",command=self.add_data,width=17,font="SUNKEN 12 bold",bg="blue",fg="white")   # command after step 4)
        save_b.grid(row=0,column=0)

        update_b = Button(b_frame,text="Update",command=self.update_data,width=17,font="SUNKEN 12 bold",bg="blue",fg="white")
        update_b.grid(row=0,column=1)

        delete_b = Button(b_frame,text="Delete",command=self.delete_data,width=17,font="SUNKEN 12 bold",bg="blue",fg="white")
        delete_b.grid(row=0,column=2)

        reset_b = Button(b_frame,text="Reset",command=self.reset_data,width=17,font="SUNKEN 12 bold",bg="blue",fg="white")
        reset_b.grid(row=0,column=3)

    
        # photo button frame
        pb_frame = Frame(cs_frame,bd=2,relief=RIDGE,bg="white")
        pb_frame.place(x=0,y=245,width=710,height=35)
        
        # buttons in photo button frame
        take_photo_b = Button(pb_frame,command=self.generate_dataset,text="Take photo sample",width=35,font="SUNKEN 12 bold",bg="blue",fg="white")         # After step 10) command will given
        take_photo_b.grid(row=0,column=0)

        update_photo_b = Button(pb_frame,text="Update photo sample",width=35,font="SUNKEN 12 bold",bg="blue",fg="white")
        update_photo_b.grid(row=0,column=1)




        # Right label frame
        r_frame = LabelFrame(m_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font="SUNKEN 12 bold")
        r_frame.place(x=780,y=10,width=720,height=560)  

        img_right=Image.open(r"images_interface\9.jpg")
        img_right=img_right.resize((710,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(r_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=710,height=130)


        # ******Search system****** in right label frame
        search_frame = LabelFrame(r_frame,bd=2,bg="white",relief=RIDGE,text="Search system information",font="SUNKEN 12 bold")
        search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(search_frame,text="Search By:",font="SUNKEN 12 bold",bg = "skyblue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font="SUNKEN 12 bold",width=15,state="read only") 
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)        
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=12,font="SUNKEN 12 bold")       
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search1_b = Button(search_frame,text="Search",width=12,font="SUNKEN 12 bold",bg="blue",fg="white")
        search1_b.grid(row=0,column=3,padx=4)

        showAll_b = Button(search_frame,text="Show All",width=12,font="SUNKEN 12 bold",bg="blue",fg="white")
        showAll_b.grid(row=0,column=4)

        # 2)
        # ******Table frame*******
        table_frame = Frame(r_frame,bd=2,bg="white",relief=RIDGE)  # Frame do not take text and font
        table_frame.place(x=5,y=210,width=700,height=320)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photosamplestatus")
        self.student_table["show"]="headings"

        # to set width
        # $
        for i in ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","photo"):
            self.student_table.column(f"{i}",width=100)
             
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)      
        self.fetch_data()      # after step 5)

    # 4)
    # ******* function declaration to save data on mysql from left frame*******

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":      
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="8771",database="newdb",port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                       
                                                                                                       self.var_dep.get(),
                                                                                                       self.var_course.get(),
                                                                                                       self.var_year.get(),
                                                                                                       self.var_sem.get(),
                                                                                                       self.var_id.get(),
                                                                                                       self.var_name.get(),
                                                                                                       self.var_div.get(),
                                                                                                       self.var_roll.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_dob.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_radio1.get()
                                                                                                       



                                                                                                                ))
                conn.commit()
                self.fetch_data()   # after step 5)
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added sucessfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


   # step 5)
   # *******Fetch data from mysql in right frame*******

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="8771",database="newdb")
        mycursor = conn.cursor()
        mycursor.execute("Select * from student")
        data = mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
     
     # step 6)
     # **** Get cursor ****

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        getdata = content["values"]
        
        # $
        a = 0
        for i in ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","radio1"):
            exec(f"self.var_{i}.set(getdata[a])")
            a+=1
        

    # step 7)
    # **** update function *****

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":       # We can do for all remaining methods by using or
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                upd = messagebox.askyesno("update","Do you want to update student details",parent = self.root)
                if upd>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="8771",database="newdb")
                    mycursor=conn.cursor()
                    mycursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Photosample=%s where student_id=%s",(            # all variables name as in mysql database before %s
                                                                                                                                                                                                         
                                                                                                                                                                                                               self.var_dep.get(),       # these variabel name as same as step 3) and 4)
                                                                                                                                                                                                               self.var_course.get(),
                                                                                                                                                                                                               self.var_year.get(),
                                                                                                                                                                                                               self.var_sem.get(),                                                                                  
                                                                                                                                                                                                               self.var_name.get(),
                                                                                                                                                                                                               
                                                                                                                                                                                                               self.var_div.get(),
                                                                                                                                                                                                               self.var_roll.get(),
                                                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                                                               self.var_dob.get(),
                                                                                                                                                                                                               self.var_email.get(),
                                                                                                                                                                                                               self.var_phone.get(),
                                                                                                                                                                                                               self.var_address.get(),                                                                                                                                                                                                          
                                                                                                                                                                                                               self.var_radio1.get(),
                                                                                                                                                                                                               self.var_id.get()         # which is to be must be in last here we consider student id
                                                                                                                                                                                                             ))
                    
                else:
                    if not upd:
                        return

                messagebox.showinfo("Sucess","Student details successfully updated",parent = self.root)   
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #  step 8)
    # ***** delete function *****

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you really want to delete data ",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="8771",database="newdb")
                    mycursor=conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted student details",parnt = self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # step 9)
    # ***** reset function *****

    def reset_data(self):
        self.var_dep.set("Selsect Department")
        self.var_course.set("Selsect Course")
        self.var_year.set("Selsect Year")
        self.var_sem.set("Selsect Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    # step 10)
    # ****** Generate dataset Take photo sample ******
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="":       
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="8771",database="newdb")
                mycursor=conn.cursor()
                mycursor.execute("Select * from student")
                myresult=mycursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                # same as in update_data
                mycursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Photosample=%s where student_id=%s",(            # all variables name as in mysql database before %s
                                                                                                                                                                                                         
                                                                                                                                                                                                               self.var_dep.get(),       # these variabel name as same as step 3) and 4)
                                                                                                                                                                                                               self.var_course.get(),
                                                                                                                                                                                                               self.var_year.get(),
                                                                                                                                                                                                               self.var_sem.get(),                                                                                  
                                                                                                                                                                                                               self.var_name.get(),
                                                                                                                                                                                                               
                                                                                                                                                                                                               self.var_div.get(),
                                                                                                                                                                                                               self.var_roll.get(),
                                                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                                                               self.var_dob.get(),
                                                                                                                                                                                                               self.var_email.get(),
                                                                                                                                                                                                               self.var_phone.get(),
                                                                                                                                                                                                               self.var_address.get(),                                                                                                                                                                                                          
                                                                                                                                                                                                               self.var_radio1.get(),
                                                                                                                                                                                                               self.var_id.get()==id+1         # only here id+=1
                                                                                                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # ***** Load predefined data on frontals from opencv *****

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")           # .xml file is in same folder no path required
                
                def face_crop(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)    # scaling factor = 1.3 & Minimum Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                    
                # to open webcam
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,myframe = cap.read()
                    if face_crop(myframe) is not None:
                        img_id +=1
                        face = cv2.resize(face_crop(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data_img/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                    
                    # to stop capturing images
                    if cv2.waitKey(1)==13 or int(img_id)==50:                              #  In waitKey "K" is Capital
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed ")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


                



    
                    




        


                





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()