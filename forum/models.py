from django.db import models
from django.contrib.auth.models import User


class Hole(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_hole')
    hole = models.CharField(max_length = 256,unique = True)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField( auto_now=True)
    def __str__(self):
        return self.hole

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_post')
    hole = models.ForeignKey(Hole,on_delete = models.CASCADE,related_name = 'hole_post')
    post = models.TextField(max_length = 1024)
    creation_datetime = models.DateTimeField( auto_now=False)
    # edition_datetime
    reply_id = models.PositiveIntegerField()
    def __str__(self):
        return self.user.username+":"+self.post
    
    
    
    
