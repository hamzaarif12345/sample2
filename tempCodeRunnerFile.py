import mysql.connector  as ms
from time import sleep
import random
import os

con=ms.connect(host="localhost",user="root",password="root81611",charset="utf8",database="accounts")

def clear_scr():
    os.system('cls')

def start():
    for i in range(0,80):
        print('*',end='')
        sleep(0.01)
    print()

def end():
    for i in range(0,80):
        print('*',end='')
        sleep(0.01)
    print()

def welcome():
    for i in ("\n\t\t\t P R O J E C T   O N   C I T Y   B A N K\n"):
        print(i,end='')
        sleep(0.02)

def create_table():
    con=ms.connect(host='localhost',user='root', password='root81611',charset='utf8',database='accounts')
    cur=con.cursor()
    st="create table if not exists acc_holder (acc_no char(5),name char(20),addr char(20),opn_bal integer,phno integer(10));"
    cur.execute(st)
    print('\n\t\t\tAccount holder table created')

def add_acc():
    cur=con.cursor()
    ch='y'
    while ch=='y':
        cur.execute('select acc_no from acc_holder')
        data=cur.fetchall()
        acno=[]
        for i in data:
            acno+=[i+[0]]
        while True:
            ac_no=random.randint(1000,5001)
            if ac_no not in acno:
                break
        print('account no=',ac_no)
        name=input('enter account holder name:')
        addr=input('enter address :')
        phno=int(input('enter phone number'))
        opening=-1
        while True:
            opening=float(input('enter opening balance='))
            if opening<1000:
                print('invalid amount....enter again')
            else:
                break
        st="insert into acc_holder (acc_no,name,addr,opn_bal,phno)values('{}','{}','{}','{}','{}')".format(ac_no,name,addr,opening, phno)
        cur.execute(st)
        con.commit()
        print('record saved...')
        ch=input('want to enter more (y/n)')
    con.close()    

def deposit():
    con=ms.connect(host='localhost',user='root',password='manager',charset='utf8',database='accounts')
    ac=input('enter account no to deposit amount')
    if con.is_connected():
                          rs='loading....'
                          print('\n\n\t\t',end='')
                          for i in rs :
                                  print(i,end='.')
                                  sleep(0.5)
                          print()
                          cur=con.cursor()
                          cur.execute('select*from acc_holder')
                          rec=cur.fetchall()
                          for i in rec:
                                     if ac in i:
                                      print ('\t',i)
                                     dep=int(input('enter amount to be deposited='))
                                     cur.execute('update acc_holder set opn_bal=opn_bal+"{}" where acc_no="{}".format(dep,ac)')
                                     con.commit()
                                     print('RECORD UPDATED SUCCESSFULLY!!')
                                     print()
def withdraw():
   con=ms.connect(host='localhost',user='root',password='manager',charset='utf8',database='accounts')
   ac=input('enter accout no to withdrawl amount')
   if con.is_connected():
                rs='LOADING....'
                print('\n\n\t\t',end='')
                for i in rs:
                                print(i,end='.')
                                sleep(0.5)
                print()
                cur=con.cursor()
                cur.execute('select*from acc_holder')
                rec=cur.fetchall()
                bal=()
                for i in rec:
                              if ac in i:
                                         print('\t',i)
                                         while True:
                                                        wtdr=int(input('enter amount to withdrawl='))
                                                        bal=i[3]-wtdr
                                                        if bal<1000:
                                                                       print('remaining balance is low')
                                                                       print('enter balance lesser than',i[3]-1000)
                                                        else:
                                                                       break
                                         cur.execute('updateacc_holder set opn_bal=opn_bal- "{} where acc_no="{}".format(wtdr,ac)')
                                         con.commit()
                                         print('RECORD UPDATED SUCCESFULLY....!!')
                                         print()
                con.close()

def updt_acc():
   con=ms.connect(host='localhost',user='root',password='manager',charset='utf8',database='accounts')
   if con.is_connected():
            rs='LOADING....'
            print('\n\n\t\t',end='')
            for i in rs :
                     print(i,end='.',sep='',)
                     sleep(0.5)
            print()
            cur=con.cursor()
            cur=execute('select*from acc_holder')
            rec=cur.fetchall()
            acno=input('enter account no to update=')
            for i in rec:
                        if acno in i:
                                print(i)
                                print()
                                print('1.update name','2.update address','3update phone number',sep='\n')
                                print()
                                print('what do you want to update')
                                while True:
                                                             ch=int(input('enter your choice:'))
                                                             if ch==1:
                                                                   nm=input('enter new name:')
                                                                   cur.execute('update  acc_holder set name="{}" where acc_no="{}".format(nm,acno)')
                                                                   break
                                                             elif ch==2:
                                                                               addr=input('enter new address:')
                                                                               cur.execute('update acc_holder set addr="{}"where acc_no="{}".format (addr,acno)')
                                                                               break
                                                             elif ch==3:
                                                                            no=int(input('enter the phone number .'))
                                                                            cur.execute ('update acc_holderset phone="{} "where acc_no="{}".format(acno)')
                                                                            break
                                                             else:
                                                                    print('INVALID CHOICE!!')
                                                                    print('RE-ENTER')
                        con.commit()
                        print('Record updated successfully')
                        con.close()


def del_acct():
    con=ms.connect(host='localhost',user='root',password='manager', charset='utf8',datbase='accounts')
    if con.is_connected():
        rs='LOADING.....'
        print('\n\n\t\t',end='')
        for i in rs:
                  print(i,end='.',sep='')
                  sleep(0.5)
        print()
        ch=input('press to see the contents')
        if ch=='s':
          cur=con.cursor()
          cur.execute('select*from acc_holder')
          rec=cur.fetchall()
          c=cur.rowcount
        print('total records-->',c)
        for i in rec:
             print(i)
        nm=input('enter ccount no t delete=')
        for i in rec:
         if nm in i:
          print('recordfound')
         print(i)
        cur.execute('delete from acc-holder where acc_no="{}".format(nm)')
        ch=input('are you sure to delete(y/n)?')         
        if ch=='y':
                                con.commit()
                                print ('RECORD DELETED SUCCESSFULLY!!')
                                print()
        con.close()


def disp_bal():
 con=ms.connect(host='localhost',user='root',password='manger',charset='utf8',database='accounts')
 cur=con.cursor()
 cur.execute('select*from acc_holder')
 rec=cur.fetchall()                      
 acno=input('enter acc no. to check the balance')
 found=False
                                
#main
                                
clear_scr()
start()                                
welcome()
end()
create_table() 
ch=1
while ch!=0:
      print('\t\t\t********main menu*********')                          
      sleep(0.50)
      print('\t\t\t1.open an account')
      sleep(0.50)
      print('\t\t\t2.deposit an amount')
      sleep(0.50)
      print('\t\t\t3.withdraw an amount')
      sleep(0.50)
      print('\t\t\t4.update the details')
      sleep(0.50)
      print('\t\t\t5.closing an account')
      sleep(0.50)
      print('\t\t\t6.balance enquiry')
      sleep(0.50)
      print('\t\t\t7. display all details')
      sleep(0.50)
      print('\t\t\t8.exit')
      sleep(0.50)
      print('\t\t\t**********')
      ch=int(input('\t\t\t enter your choice'))
      print('\t\t\t*********')
      if ch==1:
            add_acc()
            ch=input()
            clear_scr()
      elif ch==2:
            deposit()
            ch=input()
            clear_scr()
      elif ch==3:
            withdrawl()
            ch==input()
            clear_scr()
      elif ch==4:
            updt_acct()
            ch=input()
            clear_scr()
      elif ch==5:
            del_acct()
            ch=input()
            clear_scr()
      elif ch==6:
            disp_bal()
            ch=input()
            clear_scr()
      elif ch==7:
            disp_acct()
            ch=input()
            clear_scr()
      elif ch==0:
            exit()

