# User program to determine a class grade 
# this program uses user input to calculate scores 
# in 5 classes and determine their class grae 

#Asks for user name 
a = input("enter your  name : ")

#asks user for scores in each clas
b = int(input("marks in english="))
c = int(input("marks in accounts="))
d = int(input("marks in economics="))
e = int(input("marks in buisness="))
f = int(input("marks in IP="))

#total sum up all user scores and a score n is generated
#on a scale of 100
total = b+c+d+e+f
n = (total/500)*100

#The User grade is displayed based on their average score
# based on a 100 point scale
name = "Hello "+ a + " you have "
if n>=90:
    print(name, "A Grade")
elif n>=80:
    print(name, "B Grade")
elif n>=70:
    print(name, "C Grade")
elif n>=60:
    print(name, "D Grade")
elif n>=40:
    print(name, "E Grade")
else:
    print(name, "F Grade")

