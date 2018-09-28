# Q1
def mixed(var1,var2):
    extra = 0
    whole = int(var1 / var2)
    modulus = var1 % var2
    return whole +''+ modulus, "/", var2
print(mixed(25,4))

# Q2
def vowel_count(str1, vowel):
    return str1.lower().count(vowel)

vowel_count('qwertyuiasdfghxcvbnm', 'a')


# Q3
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
    area=float((4*3.14*r**3)/3)
    return area
print(area(4))

#surface area
def surface_area(r1):
    sf=0
    sf=float(4*3.14*r1**2)
    return sf
print(surface_area(6),"mm")
#Q6
def neatly(a,sf):
    return "The area and voulme of your sphere is",a,sf

print(neatly(3,4))



