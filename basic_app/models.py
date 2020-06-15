from django.db import models

class Ingredients(models.Model):
    title = models.CharField(max_length=75)

    def __str__(self):
       return self.title


       


class Post(models.Model):   
    title = models.CharField(max_length=75)
    image1 = models.ImageField(upload_to='images/' )    
    image2 = models.ImageField(upload_to='images/' ) 
    image3 = models.ImageField(upload_to='images/' ) 
    image4 = models.ImageField(upload_to='images/' )  
    image5= models.ImageField(upload_to='images/'  )   
    image6 = models.ImageField(upload_to='images/' )   
    image7 = models.ImageField(upload_to='images/' )   
    text_one = models.TextField()
    text_two = models.TextField()
    text_three = models.TextField()
    ingredients_list = models.TextField(max_length= 1500)
    ingredients = models.ManyToManyField(Ingredients)
    text_four = models.TextField()
    summary = models.TextField()

    def __str__(self):
       return self.title