from tkinter import*
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")#+0 to get it in the corner
        self.root.title("Inventory Management System")
        self.root.focus_force()

    #varaibles
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_emp_id=StringVar()
        self.var_gender= StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()


        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("arial",16),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #combobox
        cmb_search=ttk.Combobox(SearchFrame,values=("Search","Email","Name","Conatct"),state="readonly",font=("arial",16))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        text_search=Entry(SearchFrame,font=("arial,15"),fg="pink",bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame, text="Search",command=self.search,font=("arial,15"),fg="white",bg="green",cursor="hand2").place(x=410,y=10,width=150,height=30)

        title=Label(self.root,text=("Employee Details"), font=("goudy old style",15),bg="dark blue",fg="white").place(x=50,y=100,width=1000)
#row1
        lbl_empid=Label(self.root,text=("Emp_ID"),font=("goudy old style",15),bd=2,relief=RIDGE)
        lbl_empid.place(x=50,y=150)

        lbl_gender = Label(self.root, text=("Gender"), font=("goudy old style", 15), bd=2, relief=RIDGE)
        lbl_gender.place(x=350, y=150)

        lbl_contact = Label(self.root, text=("Contact"), font=("goudy old style", 15), bd=2, relief=RIDGE)
        lbl_contact.place(x=750, y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="white").place(x=150,y=150,width=180)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender, values=("Male","Female","Others"),state="readonly", font=("goudy old style", 15))
        cmb_gender.place(x=500, y=150,width=180)

        txt_contact= Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="white").place(
            x=850, y=150,width=180)

    #row2
        lbl_name = Label(self.root, text=("Name"), font=("goudy old style", 15),
                      ).place(x=50, y=190)
        lbl_dob = Label(self.root, text=("DOB"), font=("goudy old style", 15),
                         ).place(x=350, y=190)
        lbl_doj = Label(self.root, text=("DOJ"), font=("goudy old style", 15),
                         ).place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(
            x=500, y=190, width=180)
        txt_doj= Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 15), bg="lightyellow").place(
            x=850, y=190, width=180)

    #row3
        lbl_email = Label(self.root, text=("Email"), font=("goudy old style", 15),
                         ).place(x=50, y=230)
        lbl_pass = Label(self.root, text=("Password"), font=("goudy old style", 15),
                        ).place(x=350, y=230)
        lbl_utype = Label(self.root, text=("User Type"), font=("goudy old style", 15),
                        ).place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 15), bg="lightyellow").place(
            x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"),
                                  state="readonly", font=("goudy old style", 15))
        cmb_utype.place(x=850, y=230, width=180)

        #ROW4
        lbl_address= Label(self.root, text=("Address"), font=("goudy old style", 15),
                         ).place(x=50, y=270)
        lbl_salary = Label(self.root, text=("Salary"), font=("goudy old style", 15),
                          ).place(x=500, y=270)

        self.txt_address =Text(self.root,font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300,height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 15), bg="lightyellow").place(
            x=600, y=270, width=180)

        btn_add = Button(self.root, text="Save",command=self.add,font=("arial,15"), fg="white", bg="green",
                            cursor="hand2").place(x=470, y=305, width=110, height=28)
        btn_update = Button(self.root, text="Update",command=self.update,font=("arial,15"), fg="white", bg="red",
                         cursor="hand2").place(x=690,y=305, width=150, height=28)
        btn_delete = Button(self.root, text="Delete",command=self.delete,font=("arial,15"), fg="white", bg="blue",
                         cursor="hand2").place(x=810, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("arial,15"), fg="white", bg="black",
                         cursor="hand2").place(x=570, y=305, width=150, height=28)


        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"))
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="DOB")
        self.EmployeeTable.heading("doj", text="DOJ")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"]="headings"

        #self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
        #"eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"))
        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=90)
        self.EmployeeTable.column("email", width=90)
        self.EmployeeTable.column("gender", width=90)
        self.EmployeeTable.column("contact", width=90)
        self.EmployeeTable.column("dob", width=90)
        self.EmployeeTable.column("doj", width=90)
        self.EmployeeTable.column("pass", width=90)
        self.EmployeeTable.column("utype", width=90)
        self.EmployeeTable.column("address",width=90)
        self.EmployeeTable.column("salary", width=90)

        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def add(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_emp_id.get()=="":
                    messagebox.showerror("Error","Employee ID must exist",parent=self.root)
                else:
                    cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                    row=cur.fetchone()
                    if(row!=None):
                        messagebox.showerror("Error","This ID is already assigned",parent=self.root)
                    else:
                        cur.execute("INSERT INTO employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
       #self.EmployeeTable.heading("eid",text="EMP ID")")
                       # self.var_searchby = StringVar()
                       # self.var_searchtxt = StringVar()
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),

                        self.var_dob.get(),
                        self.var_doj.get(),

                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Employee added ",parent=self.root)


            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to: {str(ex)}")
            self.show()
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
              self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
      #  print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must exist", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "Invalid ID", parent=self.root)
                else:
                    cur.execute("UPDATE employee SET name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? WHERE eid=?",(

                            # self.EmployeeTable.heading("eid",text="EMP ID")")
                            # self.var_searchby = StringVar()
                            # self.var_searchtxt = StringVar()
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),




                            self.var_dob.get(),
                            self.var_doj.get(),

                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated ", parent=self.root)
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must exist", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "Invalid ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Are you sure?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")

        self.var_dob.set("")
        self.var_doj.set("")

        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        #self.txt_address.insert(END, row[9])
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input is required",parent=self.root)
            else:
             cur.execute("select * from employee where" +self.var_searchby.get()+"LIKE '%"+self.var_searchtxt.get()+"%'")
             rows = cur.fetchall()
             if len(rows)!=0:
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('', END, values=row)
             else:
                messagebox.showerror("Error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


if __name__== "__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()