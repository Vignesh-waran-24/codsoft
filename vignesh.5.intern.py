import random
while "true":
 caps_letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','h','j','k','l','l','z','x','c','v','b','n','m']
 small_letters = ['Q','W','E','R','T','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
 v_symbol=['!','@','#','$','%','^','&','*',]
 v_numbers=['1','2','3','4','5','6','7','8','9','0']

 total=caps_letters+small_letters+v_symbol+v_numbers
 length=int(input("enter a password length:"))
 password="".join(random.sample(total,length))
 print("the password is:",password)
