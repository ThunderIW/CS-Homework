def int_check(a):
    if type(a)==int:
        print('Integer')
        
    if type(a)!=int:
        print('Not Integer')
        
int_check(5.7)


#Q2
def vowel_check(word):
    print(word)
    vowelcount=0
    a=word.lower().count('a')
    vowelcount=vowelcount+1
    e=word.lower().count('e')
    vowelcount=vowelcount+1
    i=word.lower().count('i')
    vowelcount=vowelcount+1
    o=word.lower().count('o')
    vowelcount=vowelcount+1
    u=word.lower().count('u')
    vowelcount=vowelcount+1
    print(vowelcount)
    
    if vowelcount==5:
        print("your world contains all 5 vowels")
        
    if vowelcount!=5:
        print("your word dosent contain all 5 vowels")
        print(a,e,i,o,u)

    if vowelcount==0:
        print('your word dosent have any vowels')
        
vowel_check("lego")




    

    
        


