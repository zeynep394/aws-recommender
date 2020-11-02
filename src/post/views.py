from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

import pdb
import unicodedata
#imdb recommender neccesities
from pandas import read_csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame


def website(request):
    queryset=Post.objects.all()
    
    context={
        'object_list':queryset,
        
    }
    return render(request,'website.html',context)


def post(request, id):

 #importatn notes:
 # python codeumu post view fonkisyonunun içine taşıdım. Çünkü amacım python çıktısı olan recommender listesini post.htmlde göstermekti
 # bunu context kısmına recommender listesini yazarak yaptım. Böylece post fonksiyonu recommender listesini dödürüyor ve post.html dosyası bu listedeki elemanlara göre frontend çıktısı gösteriyor
 # yani her id için ayrı ayrı recommender oluşturmuş olduk
 # şuanki sorun title ı alması gereken kısımda nasıl her seferinde farklı titleı vereceğimi bilmiyor olmam. 8.10.2020 00.57    
    #a=Post.title.
    post = get_object_or_404(Post, id=id) #bu bir object id si idye eşit olan objeyi alıp post a eşitliyor eğer bulamazsa 404 döndürüyor
    

    posts = Post.objects.filter(id=id, )
    #sample_instance = Post.objects.get(pk=id)

    field_name = 'title'    
    deneme_title = getattr(posts[0], field_name) #posts bir object içinde o objeye dair title, genre release_date... gibi fieldleri bulunduryor
    #bunun 0.cısı da field name(yani title fieldi) in değeri yani"shawshank redemption gibi. yani get attribute valueyu döndürüyor ve valuemuzde string olduğu için string dönüyor
    deneme_title=deneme_title.strip()

    
    #strip yapmamızın sebebi: getattr nın getirdiği değer stringi Toy Story\xa0 şeklinde döndürüyordu bu yüzden 
    #firstidx=df[df['title'].str.strip()==title].index.tolist() kısmında Toy Story=Toy Story\xa0 olduğundan onu algılamıyor boş dönüyordu
    #striple o kısımdan kurtulduk ve hata çözüldü
    # deneme_title.replace(u'\xa0', u' ')
    #deneme_title = unicodedata.normalize("NFKD", deneme_title)

    #den_title = get_object_or_404(Post.objects.get(id=1).title, id=id)
    #d_title=deneme_title._meta.get_field('title')
    #deneme_title = d_title.value_from_object()

    #getattr(deneme_title, field.title).
    
    #deneme

    qs = Post.objects.all()
    df = read_frame(qs)
    
    #deneme_title =Post.objects.get(id=id).title

    
    def get_title_by_index(index):
        return df[df.index==index]["title"].values[0]

    
    def get_index_by_title(title):        
        firstidx=df[df['title'].str.strip()==title].index.tolist()
        strings = [str(integer) for integer in firstidx]
    
        a_string = "".join(strings)
        #pdb.set_trace()
        idx = int(a_string)
        #pdb.set_trace()
        print(idx)
        return idx


    #csv_ismi="movies_IMDb2.csv"
    #df=pd.read_csv(csv_ismi)
        
    df["genre"]=df["genre"].fillna('')
    df["director"]=df["director"].fillna('')
    df["ranking"]=df["ranking"].astype(str)

    i=0
    for i in range(250):

        df.loc[i,"director"]=df.loc[i,"director"].replace(" ","")




    def combine_features(row):
    
        return row['genre'] + " "+ row['ranking'] +" "  +row['director']+ " "+row['stars']

        
    df["combined"]=df.apply(combine_features,axis=1) 
    df["combined"].head()

    count = CountVectorizer()
    count_matrix = count.fit_transform(df['combined'])



    cosine_sim = cosine_similarity(count_matrix)

    df.index.name="index"

   
    
    page=post.title

    movie_index= get_index_by_title(deneme_title)
    #pdb.set_trace()

    similar_movies= enumerate(cosine_sim[movie_index])
    sorted_similar_movies= sorted(similar_movies, key=lambda x:x[1],reverse=True)

    recommender_list=[]
    i=0
    index_list=[]
    for movie in sorted_similar_movies:
        if i>0:
            recommender_list.append(get_title_by_index(movie[0]))
            index_list.append(movie[0])
            #pdb.set_trace()
            #recommended_movie=get_title_by_index(movie[0])
            #obje = Post.objects.get(title=recommended_movie)
            #12.10.2020 15.26
            
           
        i+=1
        if i>11:
            break 
    obje = Post.objects.filter(id__in=index_list)   
    #denembitti
    context = {
        'post':post,
        'recommender':recommender_list,
        'deneme_list':obje#bu listede sadece önerilen filmlerin isimleri var ama biz o filmi object halinde istiyoruz 
        #ki ayrı ayrı title cast falan erişebilelim title ı elde ederken yaptığımız işlemin tam tersini yapalım stringden obje elde edelim
        
    }
    return render(request, 'post.html', context)  


#def recommender(request):
    #qs = get_object_or_404(Post, id=id)


    #denembitti

 #   return recommender_list
