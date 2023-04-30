"""
Prerequisites:
    1. change host, user, password, datbase as per your system
    2. execute: "CREATE TABLE contacts(name VARCHAR(255), email VARCHAR(255), phone_no VARCHAR(255))"
    3. you are all set to run the application: open cmd in same diretory and run "python file_name"
"""
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    name = e_name.get();
    email = e_email.get();
    phone = e_phone.get();

    if(name=="" or email=="" or phone ==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con = mysql.connect(host = "localhost",user="*******",password="*******",database="python_address_book")
        cursor = con.cursor()
        cursor.execute("insert into contacts values('"+ name +"','"+ email +"','"+phone +"')")
        
        cursor.execute("commit");

        e_name.delete(0,'end')
        e_email.delete(0,'end')
        e_phone.delete(0,'end')
        MessageBox.showinfo("Insert status"," inserted successfully");
        show()
        con.close();

def delete():
    if(e_name.get() == ""):
        MessageBox.showinfo("Delete Status","Name is compulsary to delete")
    else:
        con = mysql.connect(host = "localhost",user="*******",password="*******",database="python_address_book")
        cursor = con.cursor()
        cursor.execute("delete from contacts where name ='"+ e_name.get()+"'")
        cursor.execute("commit");

        e_name.delete(0,'end')
        e_email.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("delete status"," deleted successfully");

def update():
    name = e_name.get();
    email = e_email.get();
    phone = e_phone.get();

    if(name=="" or email=="" or phone ==""):
        MessageBox.showinfo("Update Status","All Fields are required")
    else:
        con = mysql.connect(host = "localhost",user="*******",password="*******",database="python_address_book")
        cursor = con.cursor()
        cursor.execute("update contacts set email = '"+email +"',phone_no = '"+phone +"' where name ='"+name+"'")
        
        cursor.execute("commit");

        e_name.delete(0,'end')
        e_email.delete(0,'end')
        e_phone.delete(0,'end')
        show()
        MessageBox.showinfo("Update status"," Updated successfully");
        con.close();

def get():
    if(e_name.get() == ""):
        MessageBox.showinfo("Fetch Status","Name is compulsary to delete")
    else:
        con = mysql.connect(host = "localhost",user="*******",password="*******",database="python_address_book")
        cursor = con.cursor()
        cursor.execute("select * from contacts where name='"+e_name.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            e_email.insert(0,row[1])
            e_phone.insert(0,row[2])

        con.close();

def show():
     con = mysql.connect(host = "localhost",user="*******",password="*******",database="python_address_book")
     cursor = con.cursor()
     cursor.execute("select * from contacts")
     rows = cursor.fetchall()
     list.delete(0,list.size())
     for row in rows:
        insertData = row[0] + '      '+row[1]+'      '+str(row[2])
        list.insert(list.size()+1, insertData)
 
     con.close()
    
root = Tk()
root.geometry("800x400")
root.title("Python+Tkinter+mysql")

name = Label(root,text = 'Enter Name',font = ('bold',10))
name.place(x=20,y=30)

email = Label(root,text = 'Enter Email',font = ('bold',10))
email.place(x=20,y=60)

phone = Label(root,text = 'Enter Phone',font = ('bold',10))
phone.place(x=20,y=90)

e_name = Entry()
e_name.place(x=150,y=30)

e_email = Entry()
e_email.place(x=150,y=60)

e_phone = Entry()
e_phone.place(x=150,y=90)

insert = Button(root, text="insert", font=("italic",10), bg="white", command=insert)
insert.place(x=20,y=140)

delete = Button(root, text="delete", font=("italic",10), bg="white", command=delete)
delete.place(x=80,y=140)

update = Button(root, text="update", font=("italic",10), bg="white", command=update)
update.place(x=140,y=140)

get = Button(root, text="get", font=("italic",10), bg="white", command=get)
get.place(x=200,y=140)

list =Listbox(root, width=50, height=30)
list.place(x=350,y=70)
show()

root.mainloop()
