a=int(input("enter your first num:"))
b=int(input("enter your second num:"))
while "true":
 c=input("enter an operation:")
 add=a+b
 sub=a-b
 multi=a*b
 div=a/b
 mod=a%b
 if(c=="add"):
    print("add is",a+b)
 elif(c=="sub"):
    print("sub is",a-b)
 elif(c=="multi"):
    print("multi is",a*b)
 elif(c=="div"):
    print(a/b)
 elif(c=="mod"):
    print("mod is",a%B)
 else:
    print("invalid statement")
 
