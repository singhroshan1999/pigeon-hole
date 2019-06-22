from django import forms
from django.core import validators

class CreateHoleForm(forms.Form):
    hole = forms.CharField(label = "enter hole name")

class CreatePostForm(forms.Form):
    hole = forms.CharField(label = "enter hole name")
    post = forms.CharField(label = "enter post")