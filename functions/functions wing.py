# Q1
import math
def mixed(var1,var2):
    extra = 0
    whole = int(var1 / var2)
    mod = var1 % var2
    return whole,mod,"/",var2

print(mixed(25,4))

# Q2
def vowel_count(str1, vowel):
    return str1.lower().count(vowel)

vowel_count('qwertyuiasdfghxcvbnm', 'a')


# Q3

def vowel_count2(str2):
    a=str2.lower().count('a')
    e=str2.lower().count('e')
    i=str2.lower().count('i')
    o=str2.lower().count('o')
    u=str2.lower().count('u')
    return "a:",a,"e:",e,"i:",i,"o:",o,"u:",u
print(vowel_count2('Hello'))#put in the word

#Q4
def vowel_count3(str3):
    count=0
    a = str3.lower().count('a')
    count+=1
    e = str3.lower().count('e')
    count+=1
    i = str3.lower().count('i')
    count+=1
    o = str3.lower().count('o')
    count+=1
    u = str3.lower().count('u')
    count+1
    return count
print(vowel_count3("aeiouaeiou"))




#def total(str1):
    #print("in fucntions")

    #print(vowel)

    #loop = 0
    #word = str(vowel)
    #length = len(word)
    #print(length)
    #a = 0
    #e = 0
    #i = 0
    #o = 0
    #u = 0
    #while length != loop:
        # a = word.lower().count('a')
        # e = word.lower().count('e')
       # 3 i = word.lower().count('i')
       # o = word.lower().count('o')
     #   u = word.lower().count('u')
      #  loop = loop + 1
    #print("a:", a, "\ne:", e, "\ni:", i, "\no:", o, "\nu:", u)
    #choice = str(input("would like to proceed"))
    #if choice == "yes":
    #    vowel_count3(a,e,i,o,u)


# Q4
#def vowel_count3():
 #   print("in function 3")
   # totalvowel = a+e+i+o+u
  #  print("the total amount of vowels in your", word, "is:", totalvowel)


#Q5
#area
def area(r):
    area=0
    area=float((4*math.pi*r**3)/3)
    return area
print(area(4),"mm^2")

#surface area
def surface_area(r1):
    sf=0
    sf=float(4*math.pi*r1**2)
    return sf
print(surface_area(6),"mm")
#Q6
def neatly(r):
    import math
    A1=float((4*math.pi*r**3)/3)
    sf=float(4*math.pi*r**2)
    return "Your surface area and voulme of your sphere is:",A1,"mm^2",sf,"mm"
print(neatly(2))

#Q7
def cenus(name='Tim',age=-1,weight=-1):
    print(name,age,weight)


    
    
    
    


#Q8
def RGB(R,G,B):
    r=hex(R)
    g=hex(G)
    b=hex(B)
    return "Red:",r,"Green:",g,"Blue:",b

print(RGB(0,0,255))
      
def RGB_BIN(Red,Green,Blue):
    RD=bin(Red)
    GRN=bin(Green)
    BL=bin(Blue)
    return RD,GRN,BL
print(RGB_BIN(0,0,255))
    
    


    


