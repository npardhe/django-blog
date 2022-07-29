from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(blank=True,null=True,upload_to="images/profile/")
    website_url=models.CharField(max_length=200,blank=True,null=True)
    facebook_url=models.CharField(max_length=200,blank=True,null=True)
    twitter_url=models.CharField(max_length=200,blank=True,null=True)
    instagram_url=models.CharField(max_length=200,blank=True,null=True)
    pinterest_url=models.CharField(max_length=200,blank=True,null=True)

    def get_absolute_url(self): # for post
        return reverse('home')

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self): # for post
        return reverse('home')

class Post(models.Model):
    title=models.CharField(max_length=200)
    title_tag=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #body=models.TextField()
    body=RichTextField(blank=True,null=True)
    header_image=models.ImageField(blank=True,null=True,upload_to="images/")
    #post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=100,default='Coding')
    snippet=models.CharField(max_length=100)
    likes=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + '|' + str(self.author)
    def get_absolute_url(self): # for post
        return reverse('home')
        #return reverse('article-detail',args=(str(self.id)))

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()

    def __str__(self):
        return '%s - %s'%(self.post.title,self.name)