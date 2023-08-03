from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django import forms
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    summer = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    img = models.ImageField(upload_to='img/', blank=True)
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])    
    


