num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
operator = input("enter operator + - * /: ")

if operator =="+":
   res=   num1 + num2
   print(res)
elif operator =="-":
   res=   num1 - num2
   print(res)
else:
   print("wrong operator")