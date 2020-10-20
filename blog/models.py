from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #add_any additional
    Bio = models.CharField(max_length=100,default='')
    profilePic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='auth.User')
    Title = models.CharField(max_length=256)
    
    Description = RichTextField()
    
  
    post_date = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("blog:astroblog")

class BlogComment(models.Model):
    Post = models.ForeignKey(BlogPost,related_name='blogcomments',null=True,on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200,default="Visitor")
    comment_text = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentor_name
    def get_absolute_url(self):
        return reverse("blog:astroblog")

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = RichTextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("blog:home")
class AccountCancel(models.Model):
    name = models.CharField(max_length=100)
    Reason = RichTextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("blog:home")
        
class NewsPost(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default='auth.User')
    Title = models.CharField(max_length=256)
    
    Description = models.TextField()
    
    
    post_date = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse("blog:news")

class NewsComment(models.Model):
    Post = models.ForeignKey(NewsPost,related_name='newscomments',null=True,on_delete=models.CASCADE)
    commentor_name = models.CharField(max_length=200,default="Visitor")
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentor_name
    def get_absolute_url(self):
        return reverse("blog:news")