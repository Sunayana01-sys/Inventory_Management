from tkinter import*
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")#+0 to get it in the corner
        self.root.title("Inventory Management System")
        self.root.focus_force()

    #varaibles
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_invoice=StringVar()
       # self.var_gender= StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        #self.var_dob = StringVar()



        SearchFrame=LabelFrame(self.root,text="Manage Supplier Details",font=("arial",16),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #combobox
        cmb_search=ttk.Combobox(SearchFrame,values=("Search","Email","Name","Contact"),state="readonly",font=("arial",16))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        text_search=Entry(SearchFrame,font=("arial,15"),fg="pink",bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame, text="Search",command=self.search,font=("arial,15"),fg="white",bg="green",cursor="hand2").place(x=410,y=10,width=150,height=30)

        title=Label(self.root,text=("Supplier Details"), font=("goudy old style",15),bg="dark blue",fg="white").place(x=50,y=100,width=1000)
#row1
        lbl_supplier_invoice=Label(self.root,text=("Invoice No."),font=("goudy old style",15),bd=2,relief=RIDGE)
        lbl_supplier_invoice.place(x=50,y=150)


        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="white").place(x=150,y=150,width=180)
      #  cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender, values=("Male","Female","Others"),state="readonly", font=("goudy old style", 15))
       # cmb_gender.place(x=500, y=150,width=180)

        txt_contact= Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="white").place(
            x=850, y=150,width=180)

    #row2
        lbl_name = Label(self.root, text=("Name"), font=("goudy old style", 15),
                      ).place(x=50, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=190, width=180)

    #row3
        lbl_contact = Label(self.root, text=("Contact"), font=("goudy old style", 15),
                         ).place(x=50, y=230)

        txt_contact= Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=230, width=180)

  #ROW4
        lbl_desc= Label(self.root, text=("Description"), font=("goudy old style", 15),
                         ).place(x=50, y=270)


        self.txt_desc =Text(self.root,font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=150, y=270, width=300,height=60)

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

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc","contact","dob","doj","pass","utype","address","salary"))
        self.supplierTable.heading("invoice",text="EMP ID")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Email")
        self.supplierTable.heading("desc", text="Gender")


        self.supplierTable["show"]="headings"

        #self.supplierTable\ = ttk.Treeview(emp_frame, columns=(
        #"eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"))
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)


        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def add(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                if self.var_sup_invoice.get()=="":
                    messagebox.showerror("Error","Invoice must exist",parent=self.root)
                else:
                    cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                    row=cur.fetchone()
                    if(row!=None):
                        messagebox.showerror("Error","This ID is already assigned",parent=self.root)
                    else:
                        cur.execute("INSERT INTO supplier(invoice,name,contact,desc) values(?,?,?,?)",(
       #self.supplierTable.heading("eid",text="EMP ID")")
                       # self.var_searchby = StringVar()
                       # self.var_searchtxt = StringVar()
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),



                        ))
                        con.commit()
                        messagebox.showinfo("Success","Supplier added ",parent=self.root)


            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to: {str(ex)}")
            self.show()
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
              self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
      #  print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])

        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END,row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must exist", parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?,contact=?,desc=? WHERE invoice=?",(

                            # self.supplierTable.heading("eid",text="EMP ID")")
                            # self.var_searchby = StringVar()
                            # self.var_searchtxt = StringVar()
                            self.var_name.get(),

                            self.var_contact.get(),

                            self.txt_desc.get('1.0', END),
                            self.var_sup_invoice.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated ", parent=self.root)
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice number must exist", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice id=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "Invalid invoice no", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Are you sure?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier  deleted",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        #self.txt_desc.insert(END, row[9])
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=="":
                messagebox.showerror("Error","Invoice number is required",parent=self.root)

            else:
             cur.execute("select * from supplier where invoice=?" + self.var_searchtxt.get()+"%'")
             rows = cur.fetchall()
             if len(rows)!=0:
                self.supplierTable.delete(*self.supplierTable.get_children())
                for row in rows:
                    self.supplierTable.insert('', END, values=row)
             else:
                messagebox.showerror("Error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


if __name__== "__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()