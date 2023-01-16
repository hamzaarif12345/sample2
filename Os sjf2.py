def calc():
    bt1=bt.copy()
    x=min(arr)
    y=arr.index(x)
    fin[y]=bt[y]
    #print(fin[y])
    finish=0
    finish+=bt[y]
    #print("finish is",finish)
    bt.pop(y)
    
    for j in range(0,p-1):
        z=min(bt)
        print("z is",z) 
        q=bt1.index(z)
        fin[q]=finish+bt1[q]
        print("finish is ",fin[q])
        finish=finish +bt1[q]
        #print(fin[q])
        #print("finish is",finish)
        bt.remove(z)
        print(f"\n\n{fin}\n\n")
    
    print(f"Finish time are: {fin}")
    for j2 in range(0,p):
        print("Finish time at index ",j2,"is",fin[j2])
    
    print("TAT are:")
    for j1 in range(0,p,1):
        print(fin[j1],"  ",arr[j1])
        tat[j1]=(fin[j1]-arr[j1])
        print("TAT at index ",j1,"is",tat[j1])
    
    print("WT are:")
    for j1 in range(0,p,1):
        print(tat[j],"  ",bt1[j])
        wt[j1]=tat[j1]-bt1[j1]
        print("WT at index ",j1,"is",wt[j1])
    
p=int(input("Enter the number of process"))
global arr,fin,bt,tat,wt
arr=[0]*p
fin=[0]*p
bt=[0]*p
tat=[0]*p
wt=[0]*p
for i in range(0,p):
    print("Enter the arrival time of",(i+1),"process : ")
    arr[i]=int(input())
    print("Enter the CPU burst time of",(i+1),"process : ")
    bt[i]=int(input())

calc()