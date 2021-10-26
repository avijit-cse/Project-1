from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_author")
    blog_title=models.CharField(max_length=20,verbose_name="Put the title")
    slug=models.SlugField(max_length=30,unique=True)
    blog_content=models.TextField("what is your mind ?")
    blog_image=models.ImageField(upload_to='blog_image')
    publish_date=models.DateTimeField(auto_now_add=True)
    upadte_date=models.DateTimeField(auto_now=True)

 

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="blog_comment")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_comment")
    comments=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comments

class Likes(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="like_blog")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="like_user")

    def __str__(self):
        return self.user + "likes" + self.blog

