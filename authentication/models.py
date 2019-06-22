from django.db import models
from django.contrib.auth.models import User

class UserPortfolio(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'user_portfolio')
    profile_pic = models.ImageField(upload_to = 'profile_pic/',blank = True)
    portfolio_url = models.URLField()
    creation_date = models.DateField(auto_now = True)
    def __str__(self):
        return self.user.username

