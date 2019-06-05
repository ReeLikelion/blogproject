from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_data = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #길이 너무 길면, 100개로 글자를 자르고 

class Comment(models.Model):
    #1
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name="comments") 
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.CharField(max_length = 500)