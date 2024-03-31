import csv,datetime,MEMBER as membership
def schemes():
    with open("Schemes.csv","w",newline='') as f:
        writer=csv.writer(f)
        
        fields=["Scheme","Validity"]
        schemes=[["January Scheme",datetime.date(2022,1,12)],
                 ["February Scheme",datetime.date(2022,2,15)],
                 ["March Scheme",datetime.date(2022,3,1)],
                 ["April Scheme",datetime.date(2022,4,15)],
                 ["May Scheme",datetime.date(2022,5,1)],
                 ["June Scheme",datetime.date(2022,6,15)],
                 ["July Scheme",datetime.date(2022,7,16)],
                 ["August Scheme",datetime.date(2022,8,1)],
                 ["September Scheme",datetime.date(2022,9,15)],
                 ["October Scheme",datetime.date(2022,10,1)],
                 ["November Scheme",datetime.date(2022,11,15)],
                 ["December Scheme",datetime.date(2022,12,1)]]
        for i in schemes:
            writer.writerow(i)






def change():
    
    with open ("Temp.csv","w",newline='')as f:
        write=csv.writer(f)
        for i in range (0,n):
            writer.writerow(l[i])
        writer.writerow(rec)
        for j in range(n+1,len(l)):
            writer.writerow(l[i])

def filechange():
    f=open("Catalogue.csv","w",newline='')
    writer=csv.writer(f)
    f1=open("Temp.csv","r")
    reader=csv.reader(f1)
    for i in reader:
        writer.writerow(i)

    f.close()
    f1.close()
  
       
def Addtocart():
    l=[]
    f=open("Catalogue.csv","r")
    reader=csv.reader(f)
    for i in reader:
        print(i)       
        l.append(i)
           
    
    sumtotal=[]
    sumt=0
    k=int(input("Enter the number of items you want to buy --> "))
    if k !=0:
        for m in range (k):
            n=int(input("Enter the code of itmes one by one --> "))
            f=open("Temp.csv","w",newline='')
            writer=csv.writer(f)
            for i in range (0,n):
                writer.writerow(l[i])
            rec=l[n]                
            a=rec[4]
            a=int(a)-1
            rec[4]=str(a)
            b=rec[3]            
            sumtotal.append(float(b))          
            
           
                
            writer.writerow(rec)
            for j in range(n+1,len(l)):
                writer.writerow(l[j])
            f.close()

            
            f1=open("Catalogue.csv","w",newline='')
            writer1=csv.writer(f1)
            f2=open("Temp.csv","r")
            reader2=csv.reader(f2)
            for s in reader2:                
                writer1.writerow(s)
            f1.close()
            f2.close()
        for f in sumtotal:
            sumt=sumt+f
            
        print("Your Total Amount is --> ",sumt)
        return sumt
                
    else:
        print("INVALID ")
        
       
def billing():
    l1=[]
    totalprice=Addtocart()
    tdate=datetime.date.today()
    f=open("Schemes.csv","r",newline='')
    reader=csv.reader(f)
    for i in reader:       
        l1.append(i)
    for j in range (len(l1)):
        print(j,l1[j])
    mn=int(input("Enter the month number --> "))
    date=l1[mn][1]
    originalprice=totalprice
    if str(tdate) ==str(date):
        dprice=(50/100)*totalprice
        originalprice=totalprice-dprice
        print("Your total amount is ", originalprice)
    else:
        print(" No Schemes Available :( ")
    print("Membership--> Be a member and enjoy the experience of buying things at cheapest of prices")
    a=membership.main()
    if a!=None:
        print("Your total amount is --> ",originalprice-float(a))
    else:
        print("Your total amount is --> ",originalprice)


    

        
billing()



        
        
        
        
        
        
    
        
    
            
        
    
    
    

    
