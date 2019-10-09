a = input("enter the name=")
b = int(input("marks in english="))
c = int(input("marks in accounts="))
d = int(input("marks in economics="))
e = int(input("marks in buisness="))
f = int(input("marks in IP="))
total = b+c+d+e+f
n = (total/500)*100
if n>=90:
    print("A Grade")
elif n>=80:
    print("B Grade")
elif n>=70:
    print("C Grade")
elif n>=60:
    print("D Grade")
elif n>=40:
    print("E Grade")
else:
    print("F Grade")

