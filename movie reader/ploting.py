import pickle
import codecs
#Loading in the average runtime data
lodaing_runtime=open("average_runtime","rb")
runtime=pickle.load(lodaing_runtime)
print(runtime)
#loading in movie by genere
lodaing_genere=open("movie_by_genere","rb")
genere=pickle.load(lodaing_genere)
print(genere)

#using matplotlib to graph genere
import matplotlib.pyplot as plt
x=[]
y=[]
for k,v in genere.items():
    print(k,v)
    x.append(k)
    y.append(v)
plt.bar(x,y)
plt.xlabel("genere")
plt.ylabel("number of movies")
plt.title("Movie by genere")
plt.show()



#using matplotlib to graph average runtime
x_2=[]
y_2=[]

for a,b in runtime.items():
    print(a,b)
    x_2.append(a)
    y_2.append(b)


plt.bar(x_2,y_2)
plt.xlabel("Years")
plt.ylabel("Average runtime")
plt.title("Average runtime by year")
plt.show()






