from tkinter import *
from tkinter import messagebox
import csv
def Billing():
    l1=[]
    l2=[]
    l4=[]
    global E1,E2,E3,E4,E5,E6
    with open ("Catalogue.csv",'r') as f:
        reader=csv.reader(f)
        for i in reader:
            l1.append(i[3])
    for i in range(1,len(l1)):
        l2.append(float(l1[i]))
    l3=[E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get()]
    for i in l3:
        if i=='':
            l4.append(0)
        else:
            l4.append(i)
    Sumtot=int(l4[0])*l2[0]+int(l4[1])*l2[1]+int(l4[2])*l2[2]+int(l4[3])*l2[3]+int(l4[4])*l2[4]+int(l4[5])*l2[5]
    messagebox.showinfo("Bill",'Your total amount is'+str(Sumtot))
        
def Display():
    messagebox.showinfo('Instruction','Enter the quantity of itmes you wnat to buy in the respective box ...leave blank if itme is not to be bought')







def Catalogue():
    global E1,E2,E3,E4,E5,E6
    w=Toplevel(root)
    w.geometry('1200x600') 
    def prnt(lst):
        global E1,E2,E3,E4,E5,E6
        total_rows = len(lst)
        total_columns = len(lst[0])-1  
        for i in range(total_rows):
            for j in range(total_columns): 
                e = Entry(w, width=20, fg='black',
                               font=('Arial',16))
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
        Em=Entry(w,width=20,fg='black',font=('Arial',16))
        Em.insert(END,'ENTER QUANTITY *')
        Em.grid(row=0,column=4)
        E1=Entry(w,width=20,fg='black',font=('Arial',16))
        E1.grid(row=1,column=4)
        E2=Entry(w,width=20,fg='black',font=('Arial',16))
        E2.grid(row=2,column=4)
        E3=Entry(w,width=20,fg='black',font=('Arial',16))
        E3.grid(row=3,column=4)
        E4=Entry(w,width=20,fg='black',font=('Arial',16))
        E4.grid(row=4,column=4)
        E5=Entry(w,width=20,fg='black',font=('Arial',16))
        E5.grid(row=5,column=4)
        E6=Entry(w,width=20,fg='black',font=('Arial',16))
        E6.grid(row=6,column=4)
    lst=[]
    with open ("Catalogue.csv" , "r")as f:
        reader=csv.reader(f)
        for i in reader:
            lst.append(i)
    prnt(lst)
    
    B=Button(w,width=20,height=4,text='CHECKOUT',fg='black',bg='white',command=Billing).grid(row=10,column=2)
    B6=Button(w,width=20,height=4,text='INSTRUCTIONS',fg='black',bg='white',command=Display).grid(row=12,column=2)


def append():
    with open ("Registered_people.csv",'a',newline='') as f:
        username=e1.get()
        password=e2.get()
        number=e3.get()
        rec=[username,password,number]
        writer=csv.writer(f)
        writer.writerow(rec)
        messagebox.showinfo("Welcome","Have a wonderful experience :)")
        Catalogue()
        
def User():
    global e1,e2,e3
    win=Toplevel(root)
    win.geometry("900x500")
    e1=Entry(win,border=0,fg='black',bg='white',font=('Arial',11,'bold'))
    l1=Label(win,text='Enter Username').place(x=250,y=30)
    e1.place(x=250,y=50)   
    e2=Entry(win,border=0,fg='black',bg='white',show='*',font=('Arial',11,'bold'))
    l2=Label(win,text="Enter Password").place(x=250,y=70)
    e2.place(x=250,y=90)
    e3=Entry(win,border=0,fg='black',bg='white',font=('Arial',11,'bold'))
    l3=Label(win,text='Enter Phone Number').place(x=250,y=110)
    e3.place(x=250,y=130)
    B3=Button(win,text="Sign up",fg='black',bg='white',command=append).place(x=300,y=140)
    
def verify():
    global e4,e5,e6
    a=e4.get()
    b=e5.get()
    c=e6.get()
    with open ("Registered_people.csv",'r',newline='') as f:
        reader=csv.reader(f)
        username=a
        password=b
        number=c
        rec=[username,password,number]
        if rec in reader:
            messagebox.showinfo("Verified", "HAPPY SHOPPING :)")
            Catalogue()
            
        else:
            messagebox.showinfo("Not registered","User not found")
         



def Login():
    global a,b,c,e4,e5,e6
    win=Toplevel(root)
    win.geometry("900x500")
    e4=Entry(win,border=0,fg='black',bg='white',font=('Arial',11,'bold'))
    l1=Label(win,text='Enter Username').place(x=250,y=30)
    e4.place(x=250,y=50)   
    e5=Entry(win,border=0,fg='black',bg='white',show='*',font=('Arial',11,'bold'))
    l2=Label(win,text="Enter Password").place(x=250,y=70)
    e5.place(x=250,y=90)
    e6=Entry(win,border=0,fg='black',bg='white',font=('Arial',11,'bold'))
    l3=Label(win,text='Enter Phone Number').place(x=250,y=110)
    e6.place(x=250,y=130)
    B3=Button(win,text="Log in",fg='black',bg='white',command=verify).place(x=300,y=140)


  

  









root =Tk()
root.geometry("900x500")
root.title("CHANTELLE")
L1=Label(root,text='WELCOME TO CHANTELLE', font=('Algerian',50)).place(x=50,y=10)
B1=Button(root,text='SIGN UP',fg="black",bg='white',width=20,height=4,command=User).place(x=400,y=100)
L2=Label(root,text="Already registered ?",font=('Arial',11)).place(x=300,y=200)
B3=Button(root,text='LOG IN',fg='black',bg='white',width=20,height=4,command=Login).place(x=400,y=250)
root.mainloop()



