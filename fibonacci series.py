# Fibonacci series
# 0,1,1,2,3,5,8,13,21,24

def fib(n): #define the fibonacci function
    a = 0 #initial values of fibonacci sequence
    b = 1 #initial values of fibonacci sequence
    #set values
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end = " ")
        for i in range(n-2): #initial bucle for
            #fibonacci rule is xn = xn-1 + xn-2
            #          where
            #               xn is term number "n"
            #               xn-1 is the previos termn(n-1)
            #               xn-2 is the term before that (n-2)
            c = a+b
            a = b
            b = c
            print(b,end = " ")
print(fib( )) #print The Fibonacci Sequence
    
