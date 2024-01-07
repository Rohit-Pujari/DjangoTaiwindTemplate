from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

#for Blog posts 
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return "blog post by :" + self.author
    
#for comments on blog posts
class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    commentContent = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.commentContent[0:10] + " by " + self.user.username