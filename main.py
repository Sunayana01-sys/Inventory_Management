from tkinter import*
import tkinter.font as tkFont
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
class ims:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x800+0+0")#+0 to get it in the corner
        self.root.title("Inventory Management System")

#title
        normal_font = tkFont.Font(family="Arial", size=30, weight=tkFont.BOLD)
        self.image=PhotoImage(file="C:\\Users\\Sunayana\\Desktop\\ims\\logo.png")
       # title = Label(self.root,text="Inventory Management System",image=self.image,compound="RIGHT",font=normal_font),bg="#daa4aa",fg="black")
        title = Label(self.root, text="Inventory Management System",
                      font=normal_font, bg="#daa4aa", fg="black",image=self.image, compound="left",).place(x=0,y=0,relwidth=1,height=70)

#clock
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System \t\t Date:DD-MM-YYYY \t\t Time: HH:MM:SS",font=("arial",15,"bold"), bg="#000000", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
#logout
        logout_btn=Button(self.root,text="Logout",font=("Arial",15,"bold"),bg="white",cursor="hand2").place(x="1150",y="10",height="60",width="120")

 #Left menu
        self.MenuLogo=PhotoImage(file="C:\\Users\\Sunayana\\Desktop\\ims\\warehouse-management-software.png")

        leftMenu=Frame(self.root,bd=2,relief=RIDGE)
        leftMenu.place(x=0,y=102,width=200,height=565)
        Menu_logo = Label(leftMenu, image=self.MenuLogo)
        Menu_logo.pack(side=TOP,fill=X)
#buutons
        menu_btn = Button(leftMenu, text=">>Menu", font=("Arial", 20, "bold"), bg="red", cursor="hand2").pack(side=TOP,fill=X)
        employee_btn = Button(leftMenu, text=">>Employee",command=self.employee,font=("Arial", 20, "bold"), bg="purple", cursor="hand2").pack(side=TOP,
                                                                                                            fill=X)
        supplier_btn = Button(leftMenu, text=">>Supplier", command=self.supplier, font=("Arial", 20, "bold"),
                              bg="orange", cursor="hand2").pack(side=TOP,
                                                                fill=X)
        #categoru_btn = Button(leftMenu, text=">>Cateogry", font=("Arial", 20, "bold"), bg="yellow", cursor="hand2").pack(side=TOP, fill=X)
        #product_btn = Button(leftMenu, text=">>Product", font=("Arial", 20, "bold"), bg="green", cursor="hand2").pack(side=TOP,
                                                                                                            #fill=X)
        #sales_btn = Button(leftMenu, text=">>Sales", font=("Arial", 20, "bold"), bg="white", cursor="hand2").pack(side=TOP,
                                                                                                           # fill=X)
        exit_btn = Button(leftMenu, text=">>Exit", font=("Arial", 20, "bold"), bg="pink", cursor="hand2").pack(side=TOP,
                                                                                                            fill=X)

        #content
        self.lbl_employee=Label(self.root,text="Total Employee =0",bd=5,relief=RIDGE,bg="white",fg="black",font=("goudy old style",20))
        self.lbl_employee.place(x=300,y=120,height=150,width=350)

        self.lbl_supplier = Label(self.root, text="Total Supplier =0",bd=5,relief=RIDGE, bg="white", fg="black",
                                  font=("goudy old style", 20))
        self.lbl_supplier.place(x=650, y=120, height=150, width=350)

        self.lbl_category = Label(self.root, text="Total Categories =0",bd=5,relief=RIDGE, bg="white", fg="black",
                                  font=("goudy old style", 20))
        self.lbl_category.place(x=1000, y=120, height=150, width=350)

        self.lbl_product = Label(self.root, text="Total Product =0",bd=5,relief=RIDGE, bg="white", fg="black",
                                  font=("goudy old style", 20))
        self.lbl_product.place(x=300, y=300, height=150, width=350)

        self.lbl_sales = Label(self.root, text="Total Sales =0",bd=5,relief=RIDGE, bg="white", fg="black",
                                  font=("goudy old style", 20))
        self.lbl_sales.place(x=650, y=300, height=150, width=350)

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=ims(root)
    root.mainloop()