from django import forms
from django.core import validators
from forum.models import Hole,Post

# class CreateHoleForm(forms.Form):
#     hole = forms.CharField(label = "enter hole name")

# class CreatePostForm(forms.Form):
#     hole = forms.CharField(label = "enter hole name")
#     post = forms.CharField(label = "enter post")

class CreateHoleForm(forms.ModelForm):
    class Meta():
        model = Hole
        fields  = ('hole','hole_description','hole_pic')

class CreatePostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('hole','title','image','post')

class CreateReplyForm(forms.Form):
    reply = forms.CharField(label = 'enter reply')