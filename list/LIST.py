#Q1
list=[1,2,6]
list_2=[6,1,2,3]
list_3=[13,6,1,2,3]
def fool_check(var):
    for i in range(len(var)):
        print("in for loop")
        if var[i]==6 and var[0]==6 and var[-1]==6:
            return True

        else:
            return False

print(fool_check(list_3))

#Q2
list_4=[1,2,3]
list_5=[5,11,9]
List_6=[7,0,0]
rev=[]
def fool2(v):
    for i in reversed(v):
        print(i)
        rev.append(i)
    return rev

print(fool2(list_4))

#Q3
list_7 = [1, 2, 3]
first_element = []
last_element = []


def fool_3(var):
    last = var[-1]
    last_element.append(last)
    first = var[0]
    first_element.append(first)
    mergedlist=first_element+last_element
    return mergedlist
print(fool_3(list_7))

print("-------------")
#Q4
print("Question 4")
print('----------')
list_9=[2,5,3]
def fool_4(k):
    if 2 in k:
        print(True)
        p_2=k.index(2)
        print('The postion of 2==',p_2+1)

    if 3 in k:
        print(True)
        p_3=k.index(3)
        print('The postion of 3==',p_3+1)


    if 2 not in k and 3 not in k:
        print(False)


fool_4(list_9)

#Q5
print("----------")
print("Question 5")
list_10=[2,1,2,3,4]
even_number=[]
def fool_5(l):
    counter = 0
    for i in range(len(l)):
        if i%2==0:
            counter=counter+1
            even_number.append(i)
    print(counter)
    print("the even number of this list=",even_number)

fool_5(list_10)


#Q6
list_11=[1,2,2,1,13]
def fool_6(n):
    print("Orginal list:",n)
    if 13 in n:
        n.remove(13)
    print("new list:",n)
    list_total=sum(n)
    print("the sum of this list-->",list_total)

fool_6(list_11)
print("---------")


#Q7
list_12=[1,2,3,4,100]
print("Question 7")
def fool_7(H):
    print("Orginal list-->",H)
    max_num=max(H)
    min_num=min(H)

    if max_num in H:
        H.remove(max_num)

    if min_num in H:
        H.remove(min_num)

    print("new list-->",H)
    max_list=sum(H)
    print('The sum of this list-->',max_list)
    length_list=len(H)
    mean=max_list/length_list
    print('The mean of this list-->',int(mean))
print("--------------------------------------")


fool_7(list_12)


#Q7
print("Question 7")
list_13=[7,4,5,5,4,7]
rev_list=[]
def fool_8(M):
    for i in reversed(M):
        rev_list.append(i)
    print("reversed list-->",rev_list)


    if M==rev_list:
        print(True)
        print("These numbers are a palindrome",M,"==",rev_list)

    else:
        print(False)
        print("This number arent arent a palindrome")


fool_8(list_13)
print("--------------------------------------------")


print("Question 9")

upper_case=[]
new_list=[]
def fool_9(G):
    for i in range(len(G)):
        upper=G[i].upper()
        upper_case.append(upper)


    for b in upper_case:
        if b not in new_list:
            new_list.append(b)
            print(b)

        if b in new_list:
            print(G[i],'is in new_list')

    print(new_list)

fool_9(['hello', 'Hello'])






def distance(O):
    sums=[]
    postive=[]
    difference=[]
    first=10000
    second=10000


    for i in range(len(O)):
        print('coordinates',i+1)
        print('coordinates',coordiantes[i])
        total=sum(coordiantes[i])
        sums.append(total)
        print('The sum of coordiante',i+1,':',total)
        print(sums)

        postive_conversion=abs(total)
        print('postive_values',postive_conversion)
        postive.append(postive_conversion)
        print(postive)
        print('length of postive list==',len(postive))

    for b in range(0,len(postive)):
        coordiantes_postion_2 = 0
        coordiantes_postion_1 = 0
        postivediff=postive[b]-postive[b-1]
        print(b+1,postive[b],'-',postive[b-1],"difference=",postivediff)
        difference.append(abs(postivediff))
        print(abs(postivediff))
        if first==postive[b]-postive[b-1]:
            print(b)


        if second==postive[b]-postive[b-1]:
            print(b)


    for difference in difference:
        if difference<first:
            second=first
            first=difference
        elif difference>first and difference<second:
            second=difference

    print(first,second)





















print('Question 10')
coordiantes=[]
import random
def fool_10(ran):
    for i in range(0,ran):
        x=random.randint(-100,0)
        y=random.randint(-100,0)
        z=random.randint(-100,0)
        coordiantes.append([x,y,z])
        print(type(coordiantes))

        print('your 3D coordiantes_list',coordiantes)
        distance(coordiantes)

fool_10(3)