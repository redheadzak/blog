from django.db import models

class Author(models.Model):
    display_name = models.CharField(max_length=200)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self) -> str:
        return self.text

class Catagory(models.Model):
    text = models.CharField(max_length=200)
    posts = models.ManyToManyField(Post)