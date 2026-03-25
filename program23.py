a=int(input("enter first"))
b=int(input("enter sec"))
try:
    print("dev=",a/b)
except ZeroDivisionError as e:
    print("can not divide",e)
finally: 
  print("it is always")
 