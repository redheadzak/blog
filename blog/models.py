from django.db import models

class Author(models.Model):
    display_name = models.CharField(max_length=200)
        
    def __str__(self) -> str:
        return self.display_name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    @property
    def short(self):
        if len(self.text) > 200:
            return f"{self.text[:200]}..."
        return self.text

    def __str__(self) -> str:
        return self.title

class Catagory(models.Model):
    text = models.CharField(max_length=200)
    posts = models.ManyToManyField(Post)
    
    def __str__(self) -> str:
        return self.text