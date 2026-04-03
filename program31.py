import pickle
import os
def addcustomer():
   file=open('customer.bin','ab')
   cid=input("\nenter customer id :")
   cname=input("\nenter customer name :")
   cadd=input("\nenter customer addres :")
   cmobile=input("\nenter customer mobile :")
   pickle.dump(cid,file)
   pickle.dump(cname,file)
   pickle.dump(cadd,file)
   pickle.dump(cmobile,file)
   print("succesful add")
   file.close()
   input("enter continue:")
def viewallcustomer(): 
  file =open('customer.bin','rb')
  try:
    while True:
        for i in range(4):
         data=pickle.load(file)
         print('\t',data,end="")
        print()    
  except:  
         print("\n here all customer :")
  file.close() 
  input("enter continue :") 
def deletecustomer():
   file1=open('customer.bin','rb') 
   file2=open('temp.bin','ab')
   cid=input("\n   enter which id has delete :")
   try:
      while True:
          data=pickle.load(file1)
          if data==cid:
             pickle.load(file1)
             pickle.load(file1)
             pickle.load(file1)
             flag=1
          else:
             pickle.dump(data,file2)
   except:     
      if flag==0:
         print("\n not found") 
      else:
         print("\n customer delete succesful")
   file1.close()
   file2.close()
   os.remove('customer.bin')
   os.rename('temp.bin','customer.bin')
   input("\n press enitemter con")
def addproduct():
   file=open('product.bin','ab')
   pid=input("enter pid :")
   pname=input("enter pname :")
   pprice=input("enter pprice :")
   pickle.dump(pid,file)
   pickle.dump(pname,file)
   pickle.dump(pprice,file)
   file.close()
   input("\n press enter con")
def viewallproduct():
   file=open('product.bin','rb')
   try:
      while True:
       print("\n \t product ID :",pickle.load(file))
       print("\n \t pName :",pickle.load(file))
       print("\n \t pPrice:",pickle.load(file))
       print("\t **************** ")
      
   except:
      print("\n here your all  :")
      file.close()
      input("\n press enter con")
def updateproduct():
   file1=open('product.bin','rb')
   file2=open('temp.bin','ab')
   pid=input("\n \t enter product id")
   try:
      while True:
         data=pickle.load(file1)
         if data==pid:
            pickle.dump(data,file2 )
            name=pickle.load(file1)
            pickle.dump(name,file2)
            print("\t old price :",pickle.load(file1))
            price=input("\t enter new price :")
            pickle.dump(price,file2)
         else:
            pickle.dump(data,file2)
   except:
      print("\n")
   file1.close()
   file2.close()
   os.remove('product.bin')
   os.rename('temp.bin','product.bin')
def getcustomer(id_):
   cus=[]
   file=open('customer.bin','rb')

   try:
      while True:
        data= pickle.load(file)
        if data==id_:
           cus.append(data)
           cus.append(pickle.load(file))
           cus.append(pickle.load(file))
           cus.append(pickle.load(file))

   except:
       pass
   file.close()
   return cus
def getproduct(id_):
   pro=[]
   file=open('product.bin','rb')

   try:
      while True:
        data= pickle.load(file)
        if data==id_:
           pro.append(data)
           pro.append(pickle.load(file))
           pro.append(pickle.load(file))
          

   except:
       pass
   file.close()
   return pro
def placeanorder():
    cid=input("\n enter cid place to order :")
    if len(getcustomer(cid))>0:
      print("\t customer name :",getcustomer(cid)[1])
      print("\t customer address :",getcustomer(cid)[2])
      pid=input("\n enter pro id to place an order:")
      if len(getproduct(pid))>0:
        print("\t product name :",getproduct(pid)[1])
        print("\t product price :",getproduct(pid)[2])
        qty=input("enter quantity :")
        print("\n \t tot bill:",int(getproduct(pid)[2])*int(qty))
      else:
        print("\n product not found :")
     
          
    else:
       print("\n customer not found")
   
while True:
 print("\n\t \t   STUDENT RECORD SYSTEM")

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
 ch=int(input("enter your choice :"))
          
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