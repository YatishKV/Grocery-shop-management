from tkinter import *
from PIL import ImageTk, Image
import math,random
from tkinter import messagebox
import os
from tkinter import Tk, Label, Frame, Entry, Button
import sqlite3
conn = sqlite3.connect('grocerydb.sqlite')
cur = conn.cursor()


class Bill_app:
    def __init__(self, master):
        self.master=master
        

        title=Label(self.master,text="BILL DESK",bd=12,relief=GROOVE,bg="sky blue",font=("times new roman",30,"bold"),pady=2).place(relx=0,rely=0,relwidth=1,relheight=0.1)


        
        #    variable ---------------------------------------
        
        # items
        cur.execute("SELECT pro_name,pro_price FROM Product")
        self.result=cur.fetchall()
        
        self.options=[]
        self.prices={}
        for i in self.result:
            self.options.append(i[0])
            self.prices[i[0]]=i[1]

        
        self.options1=self.options[:int(len(self.options)/3)]
        self.options2=self.options[int(len(self.options)/3):int(2*len(self.options)/3)]
        self.options3=self.options[int(2*len(self.options)/3):]
        self.clicked1 = StringVar()
        self.clicked2 = StringVar()
        self.clicked3 = StringVar()
        self.clicked1.set( "Items" )
        self.clicked2.set( "Items" )
        self.clicked3.set( "Items" )

        # grocery variable
        self.qty={}
        for i in self.options:
            self.qty[i]=IntVar()

        #displaying lables
        self.i1=1
        self.i2=1
        self.i3=1
        
        #product price varible
        self.grocery_price=StringVar()
        
        # tax varible
        self.grocery_tax=StringVar()
        
        #customer details
        
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.c_add=StringVar()
        self.bill_no=StringVar()
        self.cus_id=StringVar()
        self.emp_id=StringVar()
        x=random.randint(1000,9999)
        y=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.cus_id.set(str(y))
        

        bill=cur.execute("select bill_no from Bill")
        bil_no=bill.fetchall()
        while(1):
            for i in bil_no:
                if self.bill_no in i:
                    x=random.randint(1000,9999)
                else:
                    self.bill_no.set(str(x))
                    break
            break
                
        cust=cur.execute("select cus_id from Customer")
        cus_no=cust.fetchall()
        while(1):
            for i in cus_no:
                if self.cus_id in i:
                    y=random.randint(1000,9999)
                else:
                    self.cus_id.set(str(y))
                    break
            break
        
        # ------------>>> CUSTOMER DETAILS <<<<<-----------------
        F0=LabelFrame(self.master,bd=10,relief=GROOVE,text="CUSTOMER DETAILS",font=("times new roman",15,"bold"),fg="orange red",bg="sky blue")
        F0.place(relx=0,rely=0.1,relwidth=1,relheight=0.12)
        
        cname_label=Label(F0,text="Customer Name",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F0,width=10,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cadd_label=Label(F0,text="Customer Address",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cadd_txt=Entry(F0,width=10,textvariable=self.c_add,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        cphn_label=Label(F0,text="Phone No.",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cphn_txt=Entry(F0,width=10,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        #employee id

        emp_id_label=Label(F0,text="Employee ID",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=6,padx=20,pady=5)
        emp_id_txt=Entry(F0,width=10,textvariable=self.emp_id,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=7,pady=5,padx=10)

        
                
         #----------------->>>>> Groccery frame <<<----------------
        self.F3=LabelFrame(self.master,bd=10,relief=GROOVE,text="GROCERY",font=("times new roman",15,"bold"),fg="orange red",bg="sky blue")
        self.F3.place(relx=0,rely=0.22,relwidth=0.2,relheight=0.65)

        self.drop1 = OptionMenu( self.F3 , self.clicked1, *self.options1, command = self.selected1 )
        self.drop1.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.drop1.config(font=("times new roman",15,"bold"))

        
        
        self.F4=LabelFrame(self.master,bd=10,relief=GROOVE,text=" ",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        self.F4.place(relx=0.2,rely=0.22,relwidth=0.2,relheight=0.65)

        self.drop2 = OptionMenu( self.F4 , self.clicked2, *self.options2, command = self.selected2 )
        self.drop2.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.drop2.config(font=("times new roman",15,"bold"))
        
        
        
        self.F5=LabelFrame(self.master,bd=10,relief=GROOVE,text=" ",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        self.F5.place(relx=0.4,rely=0.22,relwidth=0.2,relheight=0.65)

        self.drop3 = OptionMenu( self.F5 , self.clicked3, *self.options3, command = self.selected3 )
        self.drop3.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.drop3.config(font=("times new roman",15,"bold"))
         
        
        
        # bill Area ....................................
        
        F6=LabelFrame(self.master,bd=10,relief=GROOVE)
        F6.place(relx=0.6,rely=0.22,relwidth=0.4,relheight=0.65)
        bill_title=Label(F6,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #  bottom button frame----------------------------------
        
        F7=LabelFrame(self.master,bd=10,relief=GROOVE,text="BILL MENU",font=("times new roman",15,"bold"),fg="orange red",bg="sky blue")
        F7.place(relx=0,rely=0.87,relwidth=1,relheight=0.13)
        
        
        
        m2=Label(F7,text="Total Grocery Price",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky=W)
        m2_txt=Label(F7,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)


        # for tax
        
        tax2=Label(F7,text="Grocery Tax (5%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky=W)
        tax2_txt=Label(F7,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)


       

       
        
        total_btn=Button(F7,command=self.total,text="Total",bg="cyan",bd=5,fg="black",pady=1,width=14,font="arial 12 bold").grid(row=1,column=4,padx=15,pady=5)

        genbill_btn=Button(F7,text="Generate Bill",command=self.bill_area,bg="cyan",bd=5,fg="black",pady=1,width=14,font="arial 12 bold").grid(row=1,column=5,padx=15,pady=5)

        clear_btn=Button(F7,text="Clear",command=self.clear_data,bg="cyan",bd=5,fg="black",pady=1,width=11,font="arial 12 bold").grid(row=1,column=6,padx=15,pady=5)

        
        
        self.welcome_bill()
        

    def selected1(self,event):
        g1_label=Label(self.F3,text=self.clicked1.get(),font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=self.i1,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(self.F3,width=4,textvariable=self.qty[self.clicked1.get()],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=self.i1,column=1,padx=10,pady=10,sticky=W)
        self.i1=self.i1+1

    def selected2(self,event):
        c1_label=Label(self.F4,text=self.clicked2.get(),font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=self.i2,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(self.F4,width=4,textvariable=self.qty[self.clicked2.get()],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=self.i2,column=1,padx=10,pady=10,sticky=W)
        self.i2=self.i2+1
    
    def selected3(self,event):
        g1_label=Label(self.F5,text=self.clicked3.get(),font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=self.i3,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(self.F5,width=4,textvariable=self.qty[self.clicked3.get()],font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=self.i3,column=1,padx=10,pady=10,sticky=W)
        self.i3=self.i3+1
        
            
    def total(self):
        self.total=0.0
        self.purchased={}
        for j in self.qty.keys():
            if self.qty[j].get()!=0:
                self.purchased[j]=self.qty[j].get()
                self.total=self.total+(self.qty[j].get()*self.prices[j])
        
        self.g_tax=round((self.total*0.05),2)
        self.grocery_price.set("Rs. "+str(self.total))
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        self.total_bill=float( self.total+self.g_tax)
        
        
    def stock_update_after_purchased(self):
        prod=[]
        if self.emp_id.get()=="":
           messagebox.showerror("Error","Fill Employee ID")

        for i,j in zip(self.purchased.keys(),self.purchased.values()):
            cur.execute('select qty_in_stock from Product where pro_name = ?',(i,))
            old_stock=cur.fetchone()[0]
            new_stock=old_stock-j
            if new_stock>=0:
                cur.execute('Update Product set qty_in_stock = ? where pro_name = ?',(new_stock,i))
                prod_id=cur.execute('select pro_id from Product where pro_name = ?',(i,))
                prod.append(prod_id.fetchone()[0])
            else:
                messagebox.showerror("Error","Quantity in stock of item "+i+" is "+str(old_stock))
                return 1

        string_prod = [str(int) for int in prod]
        str_of_prod = ",".join(string_prod)
        try:
            cur.execute('insert or replace into Bill (bill_no,total_amount) values (?,?)',(int(self.bill_no.get()),int(self.total_bill)))
            cur.execute('insert into Customer (cus_id,cus_name,cus_address,emp_id,bil_no) values (?,?,?,?,?)',(int(self.cus_id.get()),str(self.c_name.get()),str(self.c_add.get()),int(self.emp_id.get()),int(self.bill_no.get())))
            cur.execute('insert into Buys (cust_id,prod_id,cus_phone_no) values (?,?,?)',(int(self.cus_id.get()),str(str_of_prod),int(self.c_phon.get())))
            conn.commit()
        except Exception as E:
            messagebox.showerror("Error",E)
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t\t|| GROCERY SHOP ||")
        self.txtarea.insert(END,"\n______________________________________________________________\n")
        self.txtarea.insert(END,f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name :   {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone no.:    {self.c_phon.get()}")
        self.txtarea.insert(END,f"\nAddress.:    {self.c_add.get()}")
        self.txtarea.insert(END,"\n====================================")
        self.txtarea.insert(END,"\nProducts\t\tQTY\t    Price")
        self.txtarea.insert(END,"\n====================================")
        
        
    def bill_area(self):
       
       if self.c_name.get()=="" or self.c_add.get()=="" or self.c_phon.get()=="":
           messagebox.showerror("Error","Fill Customer details")
       elif self.grocery_price=="Rs. 0.0":
           messagebox.showerror("Error","No product purchased")
       else: 
           
           crash=self.stock_update_after_purchased()
           if crash!=1:
               self.welcome_bill()
                #Grocery print
               for i,j in zip(self.purchased.keys(),self.purchased.values()):
                   self.txtarea.insert(END,f"\n{i}\t\t{j}\t    {str(j*self.prices[i])}")
                
               self.txtarea.insert(END,"\n`````````````````````````````````````````")
               
               if self.grocery_tax.get()!="Rs. 0.0":
                   self.txtarea.insert(END,f"\nGrocery Tax\t       {self.grocery_tax.get()}")
               
               self.txtarea.insert(END,"\n`````````````````````````````````````````")
               self.txtarea.insert(END,f"\nTotal Bill :\t      Rs. {str(self.total_bill)}") 
               self.txtarea.insert(END,"\n`````````````````````````````````````````")
               
               
               self.save_bill()
           
       
    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the bill ?")
        if op>0:
            if not os.path.exists('bills'):
                os.makedirs('bills')
            self.bill_data=self.txtarea.get('1.0',END)
            fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
            fp1.write(self.bill_data)
            fp1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved successfuly")
        else:
            return 
    
    
        
    def clear_data(self):
        
        op=messagebox.askyesno("Exit","Do you want to Clear")
        if op>0:
            
            # grocery varible
            for i in self.options:
                self.qty[i].set(0)

            #removing lables
            for widgets in self.F3.winfo_children():
                if type(widgets)!=type(self.drop1):
                    widgets.destroy()

            for widgets in self.F4.winfo_children():
                if type(widgets)!=type(self.drop2):
                    widgets.destroy()

            for widgets in self.F5.winfo_children():
                if type(widgets)!=type(self.drop3):
                    widgets.destroy()
            
            #displaying lables
            self.i1=1
            self.i2=1
            self.i3=1    

            
            #product price varible
            self.grocery_price.set("")
            
            # tax varible
            self.grocery_tax.set("")
            
            #customer details
            self.c_name.set("")
            self.c_phon.set("")
            self.c_add.set("")
            self.bill_no.set("")
            
            x=random.randint(1000,9999)
            bill=cur.execute("select bill_no from Bill")
            bil_no=bill.fetchall()
            while(1):
                for i in bil_no:
                    if self.bill_no in i:
                        x=random.randint(1000,9999)
                    else:
                        self.bill_no.set(str(x))
                        break
                break
            
            
            y=random.randint(1000,9999)
            cust=cur.execute("select cus_id from Customer")
            cus_no=cust.fetchall()
            while(1):
                for i in cus_no:
                    if self.cus_id in i:
                        y=random.randint(1000,9999)
                    else:
                        self.cus_id.set(str(y))
                        break
                break

            self.welcome_bill()
        else:
            return
                
        
    
    
    
        
        


                
class Admin_page_window:
    def __init__(self, master1):
        self.master1=master1
        
      

        self.search_bill=StringVar()

        
        
        title=Label(self.master1,text="ADMIN CONSOLE",bd=12,relief=GROOVE,bg="sky blue",font=("times new roman",30,"bold"),pady=2).place(relx=0,rely=0,relwidth=1,relheight=0.1)
        
        
        F0=LabelFrame(self.master1,bd=10,relief=GROOVE,bg="orange red")
        F0.place(relx=0,rely=0.1,relheight=0.1,relwidth=1)
        F1=LabelFrame(self.master1,bd=10,relief=GROOVE,text="MENU",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        F1.place(relx=0,rely=0.2,relwidth=0.15,relheight=0.8)
        
        bill_search=Button(F1,text="Bill Search",command=self.find_bill,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        
        bill=Entry(F1,textvariable=self.search_bill,bd=5,fg="black",width=15,font="arial 12 bold").grid(row=1,column=0,padx=10,pady=15)
        
        stock=Button(F1,text="Stock",command=self.check_stock,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=2,column=0,padx=10,pady=15)
        
        update_stock=Button(F1,text="Employee List",command=self.Employee,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=3,column=0,padx=10,pady=15)
        
        
        
        lis_of_bill=Button(F1,text="Bill List",command=self.bill_list,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=5,column=0,padx=10,pady=15)
        
        clear=Button(F1,text="Clear",command=self.clear_admin_notebook,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=6,column=0,padx=10,pady=15)
        
        
        
        
        
        # Notepad Area ....................................
        
        F4=LabelFrame(self.master1,bd=10,relief=GROOVE)
        F4.place(relx=0.15,rely=0.2,relwidth=0.85,relheight=0.8)
        bill_title=Label(F4,text="GROCERY SHOP",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.welcome_bill_admin()
        
        
        
      
        
        
        
        
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,f1.read())
                f1.close()
                present="yes"
                
                
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
    
        
        
        
    def welcome_bill_admin(self):
            
        self.txtarea.delete('1.0',END)

    def check_stock(self):
        
        self.txtarea.delete('1.0',END)
        
        self.welcome_bill_admin()
        
        self.txtarea.insert(END,"||Product id ||\t ||Quantity ||\t ||Product name ||\t ||Price(Rs.)")
        self.txtarea.insert(END,"\n_____________________________________________________________\n")
        
        cur.execute("SELECT * FROM Product")
        for j in cur.fetchall():
            self.txtarea.insert(END,f"{j[0]} \t\t {j[1]} \t\t {j[2]} \t\t    {j[3]}\n")
        self.txtarea.insert(END,'\n')
        
        
    def clear_admin_notebook(self):
        self.txtarea.delete('1.0',END)
        self.welcome_bill_admin()
    
    def bill_list(self):
        
        j=1
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"S.No.\t Bill \n\n")
        for i in os.listdir("bills/"):
           self.txtarea.insert(END,str(j)+".\t"+str(i)+"\n\n")
           j+=1
    def Employee(self):            
        self.txtarea.delete('1.0',END)
        
        self.welcome_bill_admin()
        

        
        #self.txtarea.insert(END,f1.read())
        self.txtarea.insert(END,"||Employee id ||\t ||Employee Name ||\t ||Phone No. || ||Role ||\t\t\t\t\t\t ||Sales")
        self.txtarea.insert(END,"\n________________________________________________________________________________\n")
        
        cur.execute("SELECT E.em_id,E.em_name,E.em_mobile,R.role_name,count(C.emp_id) FROM Employee E,Roles R,Customer C  WHERE E.rol_id=R.role_id AND E.em_id=C.emp_id GROUP BY C.emp_id UNION SELECT E.em_id,E.em_name,E.em_mobile,R.role_name,0 FROM Employee E,Roles R,Customer C  WHERE  E.em_id IN (SELECT em_id FROM Employee EXCEPT SELECT emp_id FROM Customer) AND E.rol_id=R.role_id ORDER BY count(C.emp_id) DESC")
        for j in cur.fetchall():
            self.txtarea.insert(END,f"{j[0]} \t\t   {j[1]}\t\t\t{j[2]} \t  {j[3]} \t\t\t {j[4]}\n")
        self.txtarea.insert(END,'\n') 


class Stock_update_app:
    def __init__(self, master):
        self.master=master

        self.p_name=StringVar()
        self.p_price=StringVar()
        self.p_stock=StringVar()

        # items
        cur.execute("SELECT * FROM Product")
        self.result=cur.fetchall()

        self.options=[]
        self.pro_name={}
        self.pro_prices={}
        self.pro_qty={}
        for i in self.result:
            self.options.append(i[2])
            self.pro_name[i[2]]=StringVar()
            self.pro_name[i[2]].set(i[2])
            self.pro_prices[i[2]]=IntVar()
            self.pro_prices[i[2]].set(int(i[3]))
            self.pro_qty[i[2]]=IntVar()
            self.pro_qty[i[2]].set(int(i[1]))
        

        self.clicked = StringVar()   
        self.clicked.set( "Items" )
        self.clicked1 = StringVar()   
        self.clicked1.set( "Items" )
        

        title=Label(self.master,text="STOCK UPDATE",bd=12,relief=GROOVE,bg="sky blue",font=("times new roman",30,"bold"),pady=2).place(relx=0,rely=0,relwidth=1,relheight=0.1)

    
        

        # ------------>>> ADD ITEM <<<<<-----------------
        F0=LabelFrame(self.master,bd=10,relief=GROOVE,text="ADD PRODUCT",font=("times new roman",15,"bold"),fg="orange red",bg="sky blue")
        F0.place(relx=0,rely=0.1,relwidth=1,relheight=0.14)
        
        pname_label=Label(F0,text="Product Name",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=0,padx=20,pady=5)
        pname_txt=Entry(F0,width=10,textvariable=self.p_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        pprice_label=Label(F0,text="Product Price",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=2,padx=20,pady=5)
        pprice_txt=Entry(F0,width=10,textvariable=self.p_price,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        pstock_label=Label(F0,text="Stock",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=4,padx=20,pady=5)
        pstock_txt=Entry(F0,width=10,textvariable=self.p_stock,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        add_item_btn=Button(F0,text="Add Item",command=self.add_item,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=15)

        # ------------>>> REMOVE ITEM <<<<<-----------------
        self.F3=LabelFrame(self.master,bd=10,relief=GROOVE,text="REMOVE PRODUCT",font=("times new roman",15,"bold"),fg="orange red",bg="sky blue")
        self.F3.place(relx=0,rely=0.24,relwidth=1,relheight=0.14)

        self.drop1 = OptionMenu( self.F3 , self.clicked1, *self.options, command = self.selected1 )
        self.drop1.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.drop1.config(font=("times new roman",15,"bold"))

        # ------------>>> STOCK UPDATE <<<<<-----------------
        self.F1=LabelFrame(self.master,bd=10,relief=GROOVE,text="UPDATE STOCK",font=("times new roman",15,"bold"),fg="orange red",bg="sky blue")
        self.F1.place(relx=0,rely=0.38,relwidth=1,relheight=0.14)

        self.drop = OptionMenu( self.F1 , self.clicked, *self.options, command = self.selected )
        self.drop.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.drop.config(font=("times new roman",15,"bold"))


        # Notepad Area ....................................
        
        F2=LabelFrame(self.master,bd=10,relief=GROOVE)
        F2.place(relx=0,rely=0.52,relwidth=1,relheight=0.48)
        bill_title=Label(F2,text="STOCK",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F2,orient=VERTICAL)
        self.txtarea=Text(F2,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.current_stock()

        
    def current_stock(self):
        self.txtarea.delete('1.0',END)
        
        self.txtarea.insert(END,"||Product id ||\t ||Quantity ||\t ||Product name ||\t ||Price")
        self.txtarea.insert(END,"\n_____________________________________________________________\n")
        
        cur.execute("SELECT * FROM Product")
        for j in cur.fetchall():
            self.txtarea.insert(END,f"{j[0]} \t\t {j[1]} \t\t {j[2]} \t\t    {j[3]}\n")
        self.txtarea.insert(END,'\n')


        
    def selected1(self,event):
        for widgets in self.F3.winfo_children():
            if type(widgets)!=type(self.drop1):
                    widgets.destroy()
                
        
        dename_label=Label(self.F3,text="Product Name",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=1,padx=20,pady=5)
        dename_txt=Entry(self.F3,width=10,textvariable=self.pro_name[self.clicked1.get()],font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=2,pady=5,padx=10)

        deprice_label=Label(self.F3,text="Product Price",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=3,padx=20,pady=5)
        deprice_txt=Entry(self.F3,width=10,textvariable=self.pro_prices[self.clicked1.get()],font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)
            
        destock_label=Label(self.F3,text="Stock",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=5,padx=20,pady=5)
        destock_txt=Entry(self.F3,width=10,textvariable=self.pro_qty[self.clicked1.get()],font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)

        delete_item_btn=Button(self.F3,text="Delete Item",command=self.delete_item,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=7,padx=10,pady=15)    


    def selected(self,event):
        for widgets in self.F1.winfo_children():
            if type(widgets)!=type(self.drop):
                    widgets.destroy()
                
        
        upname_label=Label(self.F1,text="Product Name",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=1,padx=20,pady=5)
        upname_txt=Entry(self.F1,width=10,textvariable=self.pro_name[self.clicked.get()],font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=2,pady=5,padx=10)

        upprice_label=Label(self.F1,text="Product Price",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=3,padx=20,pady=5)
        upprice_txt=Entry(self.F1,width=10,textvariable=self.pro_prices[self.clicked.get()],font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)
            
        upstock_label=Label(self.F1,text="Stock",bg="sky blue",font=("times new romen",12,"bold")).grid(row=0,column=5,padx=20,pady=5)
        upstock_txt=Entry(self.F1,width=10,textvariable=self.pro_qty[self.clicked.get()],font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)

        update_item_btn=Button(self.F1,text="Update Item",command=self.update_item,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=7,padx=10,pady=15)    

    
    def add_item(self):
        try:
            cur.execute('INSERT INTO Product(qty_in_stock, pro_name,pro_price) VALUES (?,?,?)',(int(self.p_stock.get()),self.p_name.get(),int(self.p_price.get())))
            conn.commit()
            messagebox.showinfo("Success","Item added successfully!")
            self.current_stock()
        except:
            messagebox.showerror("Error","Item already exists")

    def update_item(self):
        try:
            cur.execute('UPDATE Product SET qty_in_stock=?,pro_name=?,pro_price=? WHERE pro_name=?',(int(self.pro_qty[self.clicked.get()].get()),self.pro_name[self.clicked.get()].get(),int(self.pro_prices[self.clicked.get()].get()),self.clicked.get()))
            conn.commit()
            messagebox.showinfo("Success","Item updated successfully!")
            self.current_stock()
        except Exception as E:
            messagebox.showerror("Error",E)

    def delete_item(self):
        try:
            cur.execute('DELETE FROM Product WHERE pro_name=?',(self.clicked1.get(),))
            conn.commit()
            messagebox.showinfo("Success","Item deleted successfully!")
            self.current_stock()
        except Exception as E:
            messagebox.showerror("Error",E)


def admin_page():
    
        for widgets in frame.winfo_children():
            widgets.destroy()
        Admin_page_window(frame)
        

def Bill_page():
    
    
        for widgets in frame.winfo_children():
            widgets.destroy()
        Bill_app(frame)

def stock_update_page():
    for widgets in frame.winfo_children():
        widgets.destroy()
    Stock_update_app(frame)
        

def exit_app():
    op1=messagebox.askyesno("Exit","Do you want to Exit")
    if op1>0:
        root.destroy()
    else:
        return       


root=Tk()
root.attributes('-fullscreen', True)

frame=LabelFrame(root,bd=10,relief=GROOVE,bg='sky blue')
frame.place(relx=0,rely=0.06,relheight=0.94,relwidth=1)

menu_console=Button(root,text="Console",command=admin_page,bg="orange red",bd=5,fg="black",width=15,font="arial 12 bold").place(relx=0.005,rely=0.005,relheight=0.05)
menu_billdesk=Button(root,text="Billdesk",command=Bill_page,bg="orange red",bd=5,fg="black",width=15,font="arial 12 bold").place(relx=0.15,rely=0.005,relheight=0.05)
menu_stockupdate=Button(root,text="Stock Update",command=stock_update_page,bg="orange red",bd=5,fg="black",width=15,font="arial 12 bold").place(relx=0.295,rely=0.005,relheight=0.05)
exit_btn=Button(root,text="Exit",command=exit_app,bg="orange red",bd=5,fg="black",pady=1,width=11,font="arial 12 bold").place(relx=0.89,rely=0.005,relheight=0.05)

img = ImageTk.PhotoImage(Image.open("images1.png").convert("RGBA"))
uvce_lable=Label(frame,text="UVCE BANGALORE",font=("times new roman",16,"bold"),fg="black",bg="sky blue").place(relx=0.5,rely=0.05,anchor=CENTER)
department_lable=Label(frame,text="DEPARTMENT OF CSE",font=("times new roman",16,"bold"),fg="black",bg="sky blue").place(relx=0.5,rely=0.1,anchor=CENTER)
dbms_lable=Label(frame,text="DATABASE MANAGEMENT SYSTEM MINI PROJECT",font=("times new roman",16,"bold"),fg="black",bg="sky blue").place(relx=0.5,rely=0.15,anchor=CENTER)
grocery_lable=Label(frame,text="GROCERY SHOP MANAGEMENT",font=("times new roman",16,"bold"),fg="orange red",bg="sky blue").place(relx=0.5,rely=0.2,anchor=CENTER)
label = Label(frame, image = img).place(relx=0.5,rely=0.45,anchor=CENTER)
click_lable=Label(frame,text="Click any of the menu buttons to continue...",font=("times new roman",16,"bold"),fg="orange red",bg="sky blue").place(relx=0.85,rely=0.95,anchor=CENTER)

root.mainloop()
