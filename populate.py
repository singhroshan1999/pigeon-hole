import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","MLForum.settings")

import django
django.setup()

import random
from django.contrib.auth.models import User
from forum.models import Hole,Post
from faker import Faker
from faker import providers

fakergen = Faker()
fakergen.add_provider(providers.lorem)
users = ['user1','user2','user3','user4','user5',]

def get_user():
    return User.objects.all()[random.randint(1,5)]

def gen_fake_hole():
    for i in range(10):
        Hole.objects.create(user = get_user(),hole = fakergen.word(),
                            hole_description = fakergen.paragraph(nb_sentences=10, variable_nb_sentences=True, ext_word_list=None))

def get_hole():
    return Hole.objects.all()[random.randint(0,9)]

def gen_fake_post():
    for i in range(100):
        Post.objects.create(user = get_user(),hole = get_hole(),
                            post = fakergen.paragraph(nb_sentences=30, variable_nb_sentences=True, ext_word_list=None),
                            title = fakergen.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None))

def get_post():
    return Post.objects.all()


# gen_fake_hole()
# gen_fake_post()
# for i in range(10):
#     print(get_post())