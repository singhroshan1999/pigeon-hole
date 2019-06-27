import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","MLForum.settings")

import django
import forum.query as query
django.setup()

import random
from django.contrib.auth.models import User
from forum.models import Hole,Post,PostVoteCount
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
    return Post.objects.all()[random.randint(0,99)]
def gen_random_bool():
        return [True,True,True][random.randint(0,2)]
def gen_fake_votes():
        for i in range(100):
                p = get_post()
                u = get_user()
                if PostVoteCount.objects.filter(post = p,user = u).exists():
                        continue
                else:
                        PostVoteCount.objects.create(
                                post = p,
                                user = u,
                                is_up = gen_random_bool()
                        )
def get_fake_reply():
        post_list = Post.objects.filter(reply_id = 0).order_by('creation_datetime')[0:100]
        for i in range(100):
                post = post_list[random.randint(0,len(post_list)-1)].pk
                user = get_user()
                hole = get_hole()
                reply = Post.objects.create(user = user,hole = hole,reply_id = post,post = fakergen.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None))

def get_fake_reply_reply():
        post_list = Post.objects.exclude(reply_id = 0).order_by('creation_datetime')[0:100]
        for i in range(100):
                post = post_list[random.randint(0,len(post_list)-1)].pk
                user = get_user()
                hole = get_hole()
                reply = Post.objects.create(user = user,hole = hole,reply_id = post,post = fakergen.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None))
# gen_fake_hole()
# gen_fake_post()
# for i in range(10):
#     print(get_post())