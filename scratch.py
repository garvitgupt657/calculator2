import math
operator=input("type the operator you want to use,+,-,*,/,sqrt,**")
num1=float(input("type the first number or the base for '**' operator"))
num2=float(input("type the second number or the power for '**' operator"))
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator== 'sqrt':
    print(f"the sqrt of num one is: ",math.sqrt(num1), "the sqrt of num two is: ",math.sqrt(num2))
elif operator=="**":
    print(pow(num1,num2))
else:
    print("invalid operator")
