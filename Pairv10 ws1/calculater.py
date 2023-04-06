print("Calculator")
num1=float(input("Please enter first number:"))
num2=float(input("Please enter second number:"))
operator=input("Select your operator (+,-,/,*)")

if operator=="+":
    print(num1,"+",num2,"=",num1+num2)
elif operator=="-":
    print(num1,"-",num2,"=",num1-num2)
elif operator=="/":
    if num2==0:
        print("A number not dived by 0")
    else:
        print(num1,"/",num2,"=",num1/num2)      
elif operator=="*":
    print(num1,"*",num2,"=",num1*num2)
else:
    print("Plese give a valid operator")