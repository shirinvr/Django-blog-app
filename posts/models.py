from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=200)
  text = models.CharField(max_length=200)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.text

class Comment(models.Model):
  post=models.ForeignKey(Post, models.CASCADE)
  text = models.CharField(max_length=200)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.text