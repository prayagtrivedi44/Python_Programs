import mysql.connector 
conn=mysql.connector.connect(
host="127.0.0.1",
port=3306,
database='manage',
user='root',
password='root'
)
cur=conn.cursor()
def addcustomer():
  cname=input("\n enter name:")
  cadd=input("\n enter add:")
  cmobile=input("\n enter mobile:")
  data=(cname,cadd,cmobile)
  query="insert into customer(cname,cadd,cmobile) values(%s,%s,%s)"
  try:
   cur.execute(query,data)
   if cur.rowcount>0:
     print("\n\t customer add succeful")
   else:
     print("\n failed ")
   conn.commit()
  except:
    print("\n failed to execute")
  input("\n press continue :")
def viewallcustomer():
  query="select* from customer"
  cur.execute(query)
  data=cur.fetchall()
  print("cid  \t       cNAME  \t        CADD      \tCMOB")
  for cus in data:

    print(f"{cus[0]}".ljust(10), '\t' ,f"{cus[1]}".ljust(10), '\t' ,f"{cus[2]}".ljust(10),f"{cus[3]}".ljust(10))

    
  input("\n press continue :") 
def deletecustomer():
  cid=input("enter customer id :")
  query="select* from customer where cid="+cid
  cur.execute(query)
  data=cur.fetchone()
  if data!=None:
    print("\n\t customer name :",data[1])
    print("\n\t customer add:",data[2])
    query='delete from customer where cid='+cid
    cur.execute(query)
    if cur.rowcount>0:
      print("\n\t customer delete successful :" ) 
    else:
      print("\n\t customer failed :")
    conn.commit()
  else:
    print("\n \tcustomer not found :")
  input("\n press continue :")
def addproduct():
   pname=input("\n enter pname :")
   pprice=input("\n enter pprice :")
   data=(pname,pprice)
   query="insert into product(pname,pprice) values(%s,%s)"
   try:
     cur.execute(query,data)
     if cur.rowcount>0:
       print("\n \t product add succesful :")
     else:
       print("\n product failed :")
     conn.commit()
   except:
     print("\n product not add")
   input("\n press continue :")  
def viewallproduct():
  query="select* from product"
  cur.execute(query)
  data=cur.fetchall()
  print("PID  \t       PNAME  \t       PPRICE ")
  for pro in data:
    print(f"{pro[0]}".ljust(10), '\t' ,f"{pro[1]}".ljust(10), '\t' ,f"{pro[2]}")

  input("\n press continue :")
def updateproduct():
  pid=input("\n enter productid :")
  query="select* from product where pid="+pid
  cur.execute(query)
  pro=cur.fetchone()
  if pro!=None:
    print("\n \t product name :",pro[1])
    print("\n \t product old price:",pro[2])
    pprice=input("enter new price :")
    query="update product set pprice=%s where pid=%s"
    data=(pprice,pid)
    cur.execute(query,data)
    conn.commit()
    if cur.rowcount>0:
      print("\n update succesful :")
    else:
      print("\n faile :")
  else:
    print("\n product not update :")
  input("\n press continue :")
def placeanorder():
  cid=input("enter customer id :")
  query="select* from customer where cid="+cid
  cur.execute(query)
  cus=cur.fetchone()
  if cus!=None:
    print("\n customer name :",cus[1])
    print("\n customer add :",cus[2])
    pid=input("enter product id :")
    query="select* from product where pid="+pid
    cur.execute(query)
    pro=cur.fetchone()
    if pro!=None:
      print("\n product name:",pro[1])
      print("\n product price:",pro[2])
      quantity=input("enter qty :")
      query="insert into orders(cid,pid,quantity) values(%s,%s,%s)"
      data=(cid,pid,quantity)
      cur.execute(query,data)
      conn.commit()
      print("\n totalprice:",int(quantity)*int(pro[2 ]))
      if cur.rowcount>0:
        print("\n order succesful :")
      else:
        print("\n sorry not orderd :")
    else:
      print("\n product not availble :")
  else:
   print("\n customer not available :")
  input(" \n press continue :") 
def viewallorder():
  quary='''select cid ,cname,cadd,cmobile,pname,pprice,quantity,quantity*pprice as totalprice from customer join orders using(cid)
join product using(pid);
    '''
  cur.execute(quary)
  data=cur.fetchall()

   
  print("CID  \t       CNAME     \t   CADD     \t   CMOBILE   \t PNAME  \t PPRICE  \t QUANTITY   totalprice")
  for order in data:


   print(f"{order[0]}".ljust(10), '\t' ,f"{order[1]}".ljust(10), '\t' ,f"{order[2]}".ljust(10), '\t' ,f"{order[3]}".ljust(10), '\t' ,f"{order[4]}".ljust(10), '\t' ,f"{order[5]}".ljust(10), '\t',f"{order[6]}".ljust(10),f"{order[7]}")
  input("\n press continue :") 
def vieworderbycid():
  cid=input("\n\t enter cid where view all order :")
  quary='''select cid ,cname,cadd,cmobile,pname,pprice,quantity,quantity*pprice as totalprice from customer join orders using(cid)
join product using(pid) where cid=
    '''+cid
  cur.execute(quary)
  data=cur.fetchall()

   
  print("CID  \t       CNAME     \t   CADD     \t   CMOBILE   \t PNAME  \t PPRICE  \t QUANTITY   totalprice")
  for order in data:


   print(f"{order[0]}".ljust(10), '\t' ,f"{order[1]}".ljust(10), '\t' ,f"{order[2]}".ljust(10), '\t' ,f"{order[3]}".ljust(10), '\t' ,f"{order[4]}".ljust(10), '\t' ,f"{order[5]}".ljust(10), '\t',f"{order[6]}".ljust(10),f"{order[7]}")
  input("\n press continue :") 







while True:
 print("\n\t ##########       STUDENT MANAGEMENT SYSTEM      ###########")
 print(""" 
             1. add customer
             2. view all customer
             3. delete customer         
             4. add product
             5. view all product      
             6. update product
             7. place an order   
             8. view all order
             9. view all orders by cid
             10.exit
  """)
 ch=int(input("              enter your choice :"))
 if ch==0:
    print("bye bye")
    break
 elif ch==1:
   addcustomer()
 elif ch==2:
   viewallcustomer()
 elif ch==3:
   deletecustomer()
 elif ch==4:
   addproduct()
 elif ch==5:
   viewallproduct()
 elif ch==6:
   updateproduct()
 elif ch==7:
   placeanorder() 
 elif ch==8:
   viewallorder()
 elif ch==9:
   vieworderbycid()  
 else:
    print("\n unvalid number :")