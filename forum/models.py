from django.db import models
from django.contrib.auth.models import User

class Hole(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_hole')
    hole = models.CharField(max_length = 256,unique = True)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField( auto_now=True)
    hole_pic = models.ImageField(upload_to = 'hole_pic/',blank = True)
    hole_description = models.TextField(max_length = 1024)
    is_private = models.BooleanField(default = False)
    def __str__(self):
        return self.hole

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_post')
    hole = models.ForeignKey(Hole,on_delete = models.CASCADE,related_name = 'hole_post')
    title = models.TextField(max_length = 100)
    post = models.TextField(max_length = 1024)
    image = models.ImageField(upload_to = 'post_pic/',blank = True)
    creation_datetime = models.DateTimeField( auto_now=True)
    # edition_datetime
    reply_id = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.user.username+":"+self.post
    
class HoleFollower(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_follower')
    hole = models.ForeignKey(Hole,on_delete = models.CASCADE,related_name = 'hole_follower')
    def __str__(self):
        return self.user + self.hole
    
class PostVoteCount(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name = 'post_vote')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_vote')
    is_up = models.BooleanField(blank = False)
    def __str__(self):
        return str(self.is_up)

    
        
    
