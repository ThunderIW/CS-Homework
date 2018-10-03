#1) What is the output from the following functions?
#foo1(3, 4)
#a=3
 #b=4
#c=30
#a=4+30
#print(a)
#“43”
#foo2(5, 6)
#	b=5
#	c=6
#	a=10
#	b=10+6
#	print(b)
#	“16”

#foo3(7, 8)
#a=7
#b=20
#c=8
#c=7+20
#print(c)
#“27”

#foo1(foo2(1, 2), foo3(3, 4))
#foo2(1,2)
#b=1
#c=2

#Q2


a=10
b=20
c=30

def foo1(a,b):
    b=20
    print(a,b,c)
    a=b+c
    print(a)
foo1(2,4)

#Q4
def add(num1,num2):
    return num1+num2
def triple(num):
    return num+add(num,num)

def quad(num3):
    return num3+triple(num3)
    print()


#Q5

#Q7
#Module1 code
def say_hello(string):
   print(string)
#main code
import module1
module1.say_hello("hello")
#Q8
#Module 1 code:
def say_hello(string):
   print(string)

#Main code:
from module1 import say_hello
say_hello('Tom')
#Q9

#10
import math
print(math.log10(100))#log10
print(int(math.pow(2,3)))#power rule 2^3
print(math.sin(45))#sin 45
print(int(math.sqrt(100)))# square root(100)
print(math.pi)
