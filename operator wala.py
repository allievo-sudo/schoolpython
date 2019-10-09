# A calculator program for two numbers

#asks user for first number 
a = float(input("enter the first number="))

#Asks user for second number 
b = float(input("enter the second number="))

#asks user for desired operator 
c = input("enter the operator=")

#Prints out result based on user input 
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="**":
    print(a**b)
elif c=="//":
    print(a//b)
elif c=="%":
    print(a%b)
else:
    print("invalid operator")
