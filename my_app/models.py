from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
      title = models.CharField(max_length=200)
      subtitle = models.CharField(max_length=500)
      image =  models.ImageField(upload_to='images/')  #pip install pillow
      content = models.TextField()
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now_add=True)
      

