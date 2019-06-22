from django import forms
from django.contrib.auth.models import User
from authentication import models

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class UserPortfolioForm(forms.ModelForm):
    class Meta():
        model = models.UserPortfolio
        fields = ('profile_pic','portfolio_url')
        