def cal():
    print("inside the function")
    i=0
    while(i<total):
        for i in range (p):
            bt[i]=bt[i]-4
            fin[i]+=1
            if(bt[i]==0):
                fin1[i]=fin[i]
        i=i-4
    print("Finish time are:")
    for i in range (p):
        print("value of bt of process ",i+1,"is",fin[i])
    


p=int(input("Enter the number of process"))
global arr,fin,fin1,bt,tat,wt
arr=[0]*p
fin=[0]*p
fin1=[0]*p
bt=[0]*p
tat=[0]*p
wt=[0]*p
total=0


for i in range(0,p):
    #print("Enter the arrival time of",(i+1),"process : ")
    #arr[i]=int(input())
    print("Enter the CPU burst time of",(i+1),"process : ")
    bt[i]=int(input())

for i in range (p):
    total+=bt[i]

cal()