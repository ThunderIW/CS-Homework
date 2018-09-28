import time
import math
#given number: 9 and 7, output 2
print(9%7)#this is making use of %=modulus
print("----")
#Given number: 8 and 4,output 28
print(4*8-4)#this making use of *=power of and -=Minus
print('----')
#given number: 4,output:TRUE
print(bool(4))#making use of a Boolean statment
print("------")
#given -1,3,10,(output:14)
print(abs(-1)+10+4-1)#make use of abs=absolute value
print("------")
#given 4,4,3,(output:1)
power=(pow(4,4))
print(power%3)
print("-----")
#given 14.5,20,(output=6)
print(20-int(14.5))#make use of the int() and minus
print("-----")
#given 10,5,2.2,(outpur:false)
bo=(int(10*2.2-10*5-(10*2.2-10*5)))
print(bool(bo))
print("------")
#given 19,4,(output:(4,3))
print(divmod(19,4))#make use of divmod=a pair of numbers (a tuple) consisting of quotient q and remainder r
print("----------")
#given 5,10,13,5,(output:32)
print(str(10*5-13-5))
print("------------")
#given 4,True,15,4,output(2.0)
print(float(15%4-int(True)))
print("---------")
#question 5
#question 5,1
print(3<4 and 2>1)
print("*********")
#question 5,2
length=len("Hi")
print(length<3)
print("*******")
#queston 5,3
print(8>6 or 10<12)
print("**********")
print(not(7>10))
#question 5,4
print(5>6 and 7>8)
print("*********")
#question 5,5
print(not(6<5 and 7>8))
print("**************")
#question 5,6
print("A"!="B" and 10/5==2)
print("******************")
#question 6,6
print("A"=="B"and 10/5!=2)
print("-----------------")
#question 7
a=0
b=0
c=0
print("quadratic slover\nax^2+bx+C")
a=float(input("Type a value for a:"))
b=float(input("Type a value for b:"))
c=float(input("Type a value for c:"))
print("Sloving quadratic")
rootpart=float((b**2)-4*(a*c))
#print(rootpart)
if rootpart<0:
    print('This quadratic formula has no sloutions\n your sqaure root is:',rootpart)
rootpart2=math.sqrt(rootpart)
print(rootpart2)
root1=((-b)+(rootpart2))/2*a
root2=((-b)-(rootpart2))/2*a
print("your two x-sloutions are:",root1,"or",root2)

#question8
#logc gate
def NAND(a,b):
    if a==True:
        if b == True:
            return False
def And(a,b):
    if a==True:
        if b==True:
            return False

def OR(a,b):
    if a==True:
        return True
    elif b == True:
        return True
    else:
        return False








