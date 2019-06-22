import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","MLForum.settings")

import django
django.setup()

import random
from django.contrib.auth.models import User
from forum.models import Hole,Post
from faker import Faker

fakergen = Faker()
users = ['user1','user2','user3','user4','user5',]

def get_user():
    return User.objects.all()[random.randint(1,5)]

def gen_fake_hole():
    for i in range(10):
        Hole.objects.create(user = get_user(),hole = fakergen.company())

def get_hole():
    return Hole.objects.all()[random.randint(0,9)]

def gen_fake_post():
    for i in range(100):
        Post.objects.create(user = get_user(),hole = get_hole(),post = fakergen.text())

def get_post():
    return Post.objects.all()
# gen_fake_hole()
gen_fake_post()
for i in range(10):
    print(get_post())