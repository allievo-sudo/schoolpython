# Fibonacci series
# A program to calculate the Fibonacci sequence up to how many terms 
#the user inputs 

#fibonacci sequence is of the order  0,1,1,2,3,5,8,13,21,24

#Asks the user how many fibonacci sequence  they will like generate 
n  = int(input("Enter a number of sequence you would like too see : "))

def fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end = " ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b,end = " ")
print(fib(n))
    
