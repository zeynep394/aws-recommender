

from pandas import read_csv



import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_title_by_index(index):
    return df[df.index==index]["title"].values[0]

#buraya movie name gelecek mesela fargo [df.title==fargo]["index"] fargoyu dfde bulup indexini döndürüyor
def get_index_by_title(title):        
    firstidx=df[df['title'].str.contains(title)].index.tolist()
    strings = [str(integer) for integer in firstidx]
    
    a_string = "".join(strings)
    
    idx = int(a_string)
    print(idx)
    return idx


csv_ismi="movies.csv"
df=pd.read_csv(csv_ismi)
df



df=df.drop(["rating"],axis=1)
df

df=df.drop(["Unnamed: 0"],axis=1)
df

for col in df.columns:
    print(col, len(df[col].unique()))



df["ranking"]=df["ranking"].astype(str)



dict= {19:"Fernando Meirelles, Kátia Lund",26:" Hayao Miyazaki",28:"Peter Ramsey",39:"Olivier Nakache, Eric Toledano",46:"Rob Minkoff, Roger Allers",55:"Joe Russo, Anthony Russo",70:"Adrian Molina, Lee Unkrich",83:"Aamir Khan, Amole Gupte",93:"Gene Kelly, Stanley Donen",94:"Quentin Tarantino",105:"Terry Gilliam, Terry Jones",113:"Pete Docter",146:"Pete Docter",156:"Buster Keaton, Clyde Bruckman",157:"Ethan Coen, Joel Coen",161:"Victor Fleming",163:"Ethan Coen, Joel Coen",166:"Andrew Stanton",168:"Ethan Coen, Joel Coen",179:"Chris Sanders, Dean DeBlois",220:"Pete Docter",230:"Victor Fleming"}

for i in dict:
    df.loc[i,"director"]=dict[i]
    


df.loc[70,"runtime"]=109.0


df["genre"]=df["genre"].fillna('')


i=0
for i in range(250):
    df.loc[i,"director"]=df.loc[i,"director"].replace(" ","")


def combine_features(row):
    
    return row['genre'] + " "+ row['ranking'] +" "  +row['director']+ " "+row['cast']

        
df["combined"]=df.apply(combine_features,axis=1) 
df["combined"].head()


count = CountVectorizer()
count_matrix = count.fit_transform(df['combined'])


cosine_sim = cosine_similarity(count_matrix)


movie_index= get_index_by_title("Fargo")
print(movie_index)
    

similar_movies= enumerate(cosine_sim[movie_index])
sorted_similar_movies= sorted(similar_movies, key=lambda x:x[1],reverse=True)


i=0
for movie in sorted_similar_movies:
    if i>0:
        print(get_title_by_index(movie[0]))
    i+=1
    if i>11:
        break
