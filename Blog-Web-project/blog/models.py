from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return "blog post by :" + self.author