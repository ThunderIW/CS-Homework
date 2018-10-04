#Q1
def age_Limit(age):
    if age>=18:
        return "True"
    if age<18:
        return "False"

print(age_Limit(19))#the answer should output True
print(age_Limit(17))#The answer should output False

#Q2
def triangle(a,b,c):
    if a**2+b**2>c**2:
        print('You have an Acute angle')
    if a**2+b**2==c**2:
        print('You have Right angle triangle')

    if a**2+b**2<c**2:
        print('you have an Obtuse angle')


triangle(1,2,3)


#Q3
def div_check(num):
    if num%3==0:
        print("Fizz")

    if num%5==0:
        print("BUZZ")

    if num%3==0 and num%5==0:
        print("FIZZ,BUZZ")

    if num % 3 != 0 and num % 5 != 0:
        print("Huh?")


div_check(34)

#Q4
import math
def combinations(n,r):
    bottom=math.factorial(n-r)
    comb=math.factorial(n)/(math.factorial(r)*bottom)
    print('There are',comb,'combinations ')

    if comb==1000000:
        print('you have no chance')
    if comb>=10000 and comb<=1000000:
        print('You can do it ')

    if comb<1000:
        print('You have no chance ')



print(combinations(15,4))

#Q5
import random
ran=random.randint(-9,8)

if ran==-9:
    print("Stupid Nut Pirate")

if ran==-8:
    print("You big fat bady")

if ran==-7:
    print("Turd-face")

if ran==-6:
    print("why do you exist")

if ran==-5:
    print("you suck")


if ran==-4:
    print("")


#Q6
import random
def dice_rolling(guess1,guess2,guess3):
    guess=0
    die1=random.randint(0,5)
    die2=random.randint(0,5)
    die3=random.randint(0,5)

    if guess1==die1:
        guess=guess+1

    if guess2==die2:
        guess=guess+1

    if guess3==die3:
        guess=guess+1

    print('you have guessed',guess,'die outcomes correctly')
dice_rolling(4,5,6)









