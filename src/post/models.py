from django.db import models
from django.urls import reverse


#df=pd.read_csv("movies_IMDb.csv")
#list=[]

#for i in 
class Post(models.Model):
   
    title= models.CharField(max_length=100)
    
    genre=models.CharField(max_length=100)
    release_date=models.DateTimeField(auto_now_add=True)
    
    ranking=models.FloatField(default=0)
    director= models.CharField(max_length=100)
    stars= models.CharField(max_length=100)
    budget= models.FloatField(default=0)
    runtime= models.FloatField(default=0)
    cum_worldwide_gross= models.FloatField(default=0)
    #thumbnail = models.ImageField()
    #pic = models.ImageField(u"initial_picture",blank=True,upload_to="imdb img")
    pic = models.ImageField(blank=True)
    class Meta:
        managed = False
        db_table = 'movie_data'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
    })

#kendin df oluşturarak pandas ile yap
