from pandas import read_csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity





def get_title_by_index(index):
    return df[df.index==index]["title"].values[0]

    #buraya movie name gelecek mesela fargo [df.title==fargo]["index"] fargoyu dfde bulup indexini döndürüyor
def get_index_by_title(title):        
        #firstidx=df[df['title'].str.contains(title)].index.tolist() bu çalışıyor ama toy storyden 2 tane olduğundan iksinin indexini birleştirip yazıyor 90101 gibi
    
        #df['title'] = df['title'].str.strip()
        #firstidx=df[df['title'].str==title].index.tolist()

#------------------İMPORTANT -----------------
# önce Toy Story 3 deki aralardaki boşlukları birleştiriyoruz sonra eşitliiği kontrol ediyoruz. 
    firstidx=df[df['title'].str.strip()==title].index.tolist()
    strings = [str(integer) for integer in firstidx]
    
    a_string = "".join(strings)
    
    idx = int(a_string)
    print(idx)
    return idx


csv_ismi="movies_IMDb2.csv"
df=pd.read_csv(csv_ismi)
print(df)

count = CountVectorizer()
count_matrix = count.fit_transform(df['combined'])



cosine_sim = cosine_similarity(count_matrix)

df.index.name="index"
print(df)

df.index


movie_index= get_index_by_title("Toy Story")
    #{{post.title}})
print(movie_index)
    
print(df["title"])

similar_movies= enumerate(cosine_sim[movie_index])
sorted_similar_movies= sorted(similar_movies, key=lambda x:x[1],reverse=True)


i=0
for movie in sorted_similar_movies:
    if i>0:
        print(get_title_by_index(movie[0]))
    i+=1
    if i>11:
        break