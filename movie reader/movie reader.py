import codecs
movie_attributes=[]
movive_data=[]
sentences=[]

with codecs.open("movies.txt","r",encoding="utf-8") as f:
    first_line=f.readline()
    print(first_line)
    attributes=first_line.strip().split(';')
    movie_attributes.append(attributes)
    print(movie_attributes)


    f.readline()
    for line in f.readlines():
        line=line.strip().split(';')
        #print(line)
        movive_data.append(tuple(line))

    #print(line)
    #print(movive_data)
    #print(len(movive_data))

with codecs.open("movies.tsv","w",encoding='utf-8')as f:
    for movie in movive_data:
        for item in movie:
            item= item.replace('\t','')
            string_list=str(item)
            f.write(item+"\t")
        f.write('\n')

by_year={}
by_director={}
by_actor={}
by_actress={}
by_subject={}


for movie in movive_data:
    if movie[0] in by_year:
        by_year[movie[0]].append(movie)

    if movie[6] in by_director:
        by_director[movie[6]].append(movie)

    if movie[5] in by_actress:
        by_actress[movie[5]].append(movie)

    if movie[4] in by_actor:
        by_actor[movie[4]].append(movie)


    if movie[3] in by_subject:
        by_subject[movie[3]].append(movie)



    else:
        #str              #tuple
        by_year[movie[0]]=[movie]
        by_director[movie[6]]=[movie]
        by_actor[movie[4]]=[movie]
        by_actress[movie[5]]=[movie]
        by_subject[movie[3]]=[movie]





#average runtime of movie by year[1]
import pickle

average_runtime={}
count_byyear={}
movie_counter=0
time=0
for year in by_year:
    count=0
    time=0
   # print(year,count)
    for movie in by_year[year]:
        if movie[1].isdigit():
            time+=int(movie[1])
            count+=1


        average=int(time/count)
        #print('average runtime for ',year,'is:',average)
        average_runtime[year]=average
        pickle_out=open("average_runtime","wb")
        pickle.dump(average_runtime,pickle_out)
        pickle_out.close()



#number of movies per genre
#postion=3(genre)

movie_by_genere={}
rejected={}
for genre in by_subject:
    gen=movie_by_genere[genre]=len(by_subject[genre])
    print(gen, ":", genre)
    movie_by_genere[genre]=len(by_subject[genre])
    if genre=='':
        print(gen,':', "no data")
    if '' in movie_by_genere:
        del movie_by_genere['']
        pickle_out_2=open("movie_by_genere","wb")
        pickle.dump(movie_by_genere,pickle_out_2)

print(movie_by_genere)
