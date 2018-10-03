

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







