from forum.models import Hole,Post
from authentication.models import UserPortfolio
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_post(start = 0,end = 10,user = None,hole = None):
    post = {}
    if user is None and hole is None:
        post['post'] = Post.objects.filter(reply_id = 0).order_by('-creation_datetime')[start:end]
    elif user is not None and hole is not None:
        if User.objects.filter(username = user).exists() and Hole.objects.filter(hole = hole).exists():
            user = User.objects.filter(username = user)[0]
            hole = Hole.objects.get(hole = hole)
            post['post'] = Post.objects.filter(reply_id = 0,user = user,hole = hole).order_by('-creation_datetime')[start:end]
    elif user is not None:
        if User.objects.filter(username = user).exists():
            user = User.objects.filter(username = user)[0]
            post['post'] = Post.objects.filter(reply_id = 0,user = user).order_by('-creation_datetime')[start:end]
    elif hole is not None:
        if Hole.objects.filter(hole = hole).exists():
            hole = Hole.objects.get(hole = hole)
            post['post'] = Post.objects.filter(reply_id = 0,hole = hole).order_by('-creation_datetime')[start:end]
    return post

def get_hole(start = 0,end = 10,user = None,order_by_modified = True):
    hole = {}
    if order_by_modified:
        order = '-modified_date'
    else:
        order = '-creation_date'
        
    if user is None:
        hole['hole'] = Hole.objects.order_by(order)[start:end]
    elif user is not None:
         if User.objects.filter(username = user).exists():
            user = User.objects.get(username = user)
            hole['hole'] = Hole.objects.filter(user = user).order_by(order)[start:end]
    return hole

def get_user(start = 0,end = 10):
    return UserPortfolio.objects.all()[start:end]

# @login_required
def create_hole(username,hole):
    if Hole.objects.filter(hole = hole).exists() == False:
        user = User.objects.get(username = username)
        h = Hole.objects.create(user = user,hole = hole)
        h.save()
        return True
    else:
        return False
            # already exist

def create_post(username,hole,post):
    if Hole.objects.filter(hole = hole).exists() == False:
        create_hole(username,hole)
    h = Hole.objects.get(hole = hole)
    user = User.objects.get(username = username)
    p = Post.objects.create(user = user,hole = h,post = post)
    p.save()

# def get_profile(username)

    
    