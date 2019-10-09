a = input("enter the name=")           # Get a string input as 'a' from console
b = int(input("marks in english="))    # Get a string input as 'b' from console and cast(convert) it to integer
c = int(input("marks in accounts="))   # Get a string input as 'c' from console and cast(convert) it to integer
d = int(input("marks in economics="))  # Get a string input as 'd' from console and cast(convert) it to integer
e = int(input("marks in buisness="))   # Get a string input as 'e' from console and cast(convert) it to integer
f = int(input("marks in IP="))         # Get an input a string 'f' from console and cast(convert) it to integer
total = b+c+d+e+f       # Get the sum of all b,c,d,e,f and assign it to total(int)
n = (total/500)*100     # Divide the total by 500 and multiply it by 100 and assign the value to n
if n>=90:               # If the value of n is greater than or equal to 90
    print("A Grade")    # Print 'A  Grade' on the console
elif n>=80:             # If the value of n is greater than or equal to 80
    print("B Grade")    # Print 'B  Grade' on the console
elif n>=70:             # If the value of n is greater than or equal to 70
    print("C Grade")    # Print 'C  Grade' on the console
elif n>=60:             # If the value of n is greater than or equal to 60
    print("D Grade")    # Print 'D  Grade' on the console
elif n>=40:             # If the value of n is greater than or equal to 40
    print("E Grade")    # Print 'E  Grade' on the console
else:                   # If all the above conditions are false
    print("F Grade")    # Print 'F  Grade' on the console

