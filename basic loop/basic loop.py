#Q1
#while loop
loop=12#REASON BEING THAT O IS THE STARTING VALUE INSTEAD OF 1
num=8
count=0
print("outside of loop")


while count!= loop:
    print("in loop")
    print("current number:",num)
    num-=1
    count+=1
print("-----------------------")

#FOR LOOP

for i in range(-3,8):
    print("Current number:",i)

print("---------------------")

#Q2

def is_odd(num):
    if num%2==0:
        return False,":even" #num is even

    if num %2!=0:
        return True,":odd" #number is odd

    else:
        print("Not even or odd")


for i in range(1,11):
    print(i)
    print("Number is",is_odd(i))
print("-----------------------")


#Q3
def dice_roll(rolls):
    store1=0
    store2=0
    store3=0
    store4=0
    store5=0
    store6=0
    print(rolls)
    print("Begin rolling")
    for i in range(1,rolls):
        print(i)
        import random
        sim=random.randint(1,6)
        print(sim)
        print("Rolls-->",i)
        if sim==1:
            store1+=1
        if sim==2:
            store2+=1
        if sim==3:
            store3+=1
        if sim==4:
            store4+=1
        if sim==5:
            store5+=1
        if sim==6:
            store6+=1

    print("----Done rolling----" )
    print("number of 1-->",store1,"\nnumber of 2-->",store2,"\nnumber of 3-->",store3,"\nnumber of 4-->",store4,"\nnumber of 5-->",store5,"\nnumber of 6-->",store6)

print(dice_roll(rolls))#rolls can be anything you want 

#Q4
def check(number):
    n = str(number)
    num_list = list(n)
    print(num_list)

    for i in num_list:
        intger=int(i)
        print(type(intger))

        if intger%2==0:
            print(i,'--> even')
        if intger%2!=0:
            print(i,'--> odd')
check(63)









