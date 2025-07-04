from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=120)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f'Comment by {self.author.username}'