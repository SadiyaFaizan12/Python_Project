import csv
def createmem():
    with open("Membership.csv","w",newline='') as f:
        writer=csv.writer(f)
        fields=["Number","Name","Points"]
        writer.writerow(fields)
        rows=[["9958305511","ABC","400"],['8587994747','DEF','241']]
        writer.writerows(rows)
def memamount():
    l1=[]
    d1={}   
    num=input("Enter your registered phone number(again) --> ")
    with open("Membership.csv","r",newline='') as f:
        reader=csv.reader(f)
        for i in reader:
            l1.append(i)
        for j in l1:
            d1[str(j[0])]=[str(j[1]),str(j[2])]
    l4=d1.keys()    
    l3=d1.values()
    f=open("temp0.csv","w",newline='')
    writer=csv.writer(f)
    
        
    for i in l4:
        if i!= num:
            #print([i,d1[i][0],d1[i][1]])
            writer.writerow([i,d1[i][0],d1[i][1]])
    rec=d1[num]               
    a=rec[1]
    print("Number of points available -->",d1[num][1])
    while True:
        point=int(input("Enter the number of points you want to use --> "))
        if point<int(d1[num][1]):
            a=int(a)-point
            print("Points left --> ",a)
            break
        else:
            print("Not Enough points ....want to quit??(Q) or Try again(T)")
            ch=input()
            if ch=='Q':
                break
            else:
                continue
    
    rec[1]=str(a)
    writer.writerow([num,rec[0],rec[1]])
    f.close()
        
        
    f1=open("Membership.csv","w",newline='')
    writer1=csv.writer(f1)
    f2=open("temp0.csv","r")
    reader2=csv.reader(f2)
    for s in reader2:                
        writer1.writerow(s)
    f1.close()
    f2.close()
    return point     
        

def member():
    with open("Membership.csv","a",newline='') as f:
        name=input("Enter your name --> ")
        number=input("Enter your phone number --> ")
        points="10000"
        list=[number,name,points]
        writer=csv.writer(f)
        writer.writerow(list)
    print("Registered\nHappy Shopping\n\n")
    a= memamount()
    return a


    
def verifymem():
    l1=[]
    l2=[]
    f=open("Membership.csv","r")
    reader=csv.reader(f)
    for i in reader:
        l1.append(i)
    for j in range (1,len(l1)):
        l2.append(l1[j][0])
    while True:
        num=input("Enter your contact number --> ")
        if num in l2:
            u=memamount()
            return u
        
        else:
            print("Number not registered as a member :( ")
            ch = input("Want to try again?\nWant to register again(R/r)\nEnter y/Y if yes\n--> ")
            if ch in "Yy":
                continue
            elif ch in "Rr":
                 l= member()
                 return l
            else:
                break
        
    
    

                   
               


def main(): 

    ans=input("Do you have a membership? Yy/Nn\n--> ")
    if ans[0].lower=="y":
        b=verifymem()
        return b
    
    else:
        while True:
            a=input("Do you want to become a lifetime member for only INR 1000/- ? Y/N")
            if a[0].lower()=='y':
                c=member()
                return c
            
            else:
                break
 


