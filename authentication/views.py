from django.shortcuts import render
from authentication import forms
import random

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user = forms.UserForm(request.POST)
        user_portfolio = forms.UserPortfolioForm(request.POST)
        if user.is_valid() and user_portfolio.is_valid():
            user = user.save( commit = True )  # saves user form to database
            user.set_password(user.password)
            user.save()
            user_portfolio = user_portfolio.save(commit = False)  # saves user portfolio to temp variable
            user_portfolio.user = user
            if 'profile_pic' in request.FILES:
                fileName = request.FILES['profile_pic'].name
                request.FILES['profile_pic'].name = str(random.randint(1,10000)*random.randint(1,10000)) + fileName[fileName.rfind('.'):]
                user_portfolio.profile_pic = request.FILES['profile_pic']
            user_portfolio.save() # store user form to database
            # profile pic....
        else:
            print('INVALID AUTH REG')
    else:
        user = forms.UserForm()
        user_portfolio = forms.UserPortfolioForm()
    return render(request, 'authentication/register.html',{'user_form':user,'portfolio':user_portfolio})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                print('SUCCESSFUL')
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('inactive user')
        else:
            print(username,password,user)
            return HttpResponse('user dont exist')
    else:
        return render(request,'authentication/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
