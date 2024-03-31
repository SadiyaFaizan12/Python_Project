import csv,SCHEMES as Schemes , random

def randpas():
    f=open("Pass.txt","r")
    r=f.read().split(' ')
    f.close()
    f=open("Pass.txt","a")
    while True:
        i =str(random.randrange(1000,2000))
        if i in r:
            i=str(random.randrange(1000,2000))
            continue
        else:
            f.write(i+'\n')
            f.close()
            return i
        
        
def createadmin():
    
    with open ("Admin.csv","w",newline='') as f:
        writer=csv.writer(f)
        fields=["ID","NAME","PASSWORD"]
        writer.writerow(fields)
        rows=[["101","Sadiya","1234"],
              ["102","Kareena","5678"]]
        for i in rows:
            writer.writerow(i)


def addadmin():
    l1=[]
    n=int(input("Enter the number of new entries --> "))
    print("Enter the details for each entry 1 by 1")
    for i in range (n):
        print("Entry",i+1)
        ID=input("Enter ID --> ")
        name=input("Enter Name --> ")
        pas=randpas()
        print("Password is",pas)
    with open ("Admin.csv","a",newline='') as f:
        writer=csv.writer(f)
        en=[ID,name,pas]
        writer.writerow(en)


def verifyadmin():
    a=input("Enter ID --> ")
    b=input("Enter Name --> ")
    c=input("Enter Password --> ")
    with open("Admin.csv","r")as f:
        reader=csv.reader(f)
        ID=str(a)
        Name=str(b)
        Pass=str(c)
        rec=[ID,Name,Pass]
        
        if rec in reader:
            print ("ACCESS GIVEN !!")
            print()
            adminfunctions()
        else:
            print("ACCESS DENIED !!")
def adminfunctions():
       
    print()
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print()
    print("1.UPDATE THE CURRENT CATALOGUE")
    print("2. ADD NEW ADMINS")
    with open ("Catalogue.csv" , "r")as f:
        print("CURRENT CATALOGUE")
        print()
        reader=csv.reader(f)
        for i in reader:
            print(i)                  
    print()
    while True:
        ch=int(input("Enter your choice --> "))
        if ch==1:            
            updatecatalogue()
        elif ch==2:
            addadmin()
        else:
            print("Invalid Choice!!")
        choice=input("Do you wish to continue? --> ")
        if choice[0].lower() == 'y':
            continue
        elif choice[0].lower() == 'n':
            break
        else :
            print("Invalid Choice!!")
            break    

def updatecatalogue():
    with open ("Catalogue.csv","a",newline='')as f:
        writer=csv.writer(f)
        fields=["ITEM CODE","ITEM NAME","BRAND","ITEM PRICE","QUANTITY LEFT"]
        #writer.writerow(fields)
        n=int(input("Enter the number of records you want to add --> "))
        for i in range (n) :
            icode=input("Enter Item code --> ")
            iname=input("Enter Item name --> ")
            ibrand=input("Enter Item Brand --> ")
            iprice=float(input("Enter Item price --> "))
            Qnt=int(input("Enter quantity  --> "))
            rec=[icode,iname,ibrand,iprice,Qnt]
            writer.writerow(rec)



verifyadmin()
    
