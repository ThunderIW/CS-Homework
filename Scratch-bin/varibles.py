a=float(1)
b=int(2)
c=bool(False)
d=str('HI')

print(type(a),type(b),type(c),type(d))
print(a,b,c,d)
print(bool(a),bool(b),bool(c),bool(d))
sumbool=bool(a+b+c+len(d))
sumfloat=float(a+b+c+len(d))
print(sumbool)
print(sumfloat)
print(int(sumbool))
print(int(sumfloat))
print(chr(97))#varaibles need to be chr(x)=>97
print(ord('a'))