import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","MLForum.settings")

import django
import forum.query as query
django.setup()

import random
from django.contrib.auth.models import User
from forum.models import Hole,Post,PostVoteCount
from authentication.models import UserPortfolio
from faker import Faker
from faker import providers

fakergen = Faker()
fakergen.add_provider(providers.lorem)
fakergen.add_provider(providers.person)
fakergen.add_provider(providers.profile)
fakergen.add_provider(providers.internet)
users = ['user1','user2','user3','user4','user5',]

def get_user():
    return random.choice(User.objects.all())

def gen_fake_hole(n = 10):
    hole_pic = ['14745600.jpg','56869128.jpg','download.jpg']
    print('-=-=-=-=-=-=-=-=-=GENERATING=-=-=-=-=-=-=-=-=-')
    print('0%')
    for i in range(n):
        Hole.objects.create(user = get_user(),hole = fakergen.word(),
                            hole_description = fakergen.paragraph(nb_sentences=10, variable_nb_sentences=True, ext_word_list=None),
                            hole_pic = '/hole_pic/'+hole_pic[random.randint(0,len(hole_pic)-1)])
        if i%(n//10) == 0:
                print(str(i)+' completed')
    print('-=-=-=-=-=-=-=-=-=COMPLETED=-=-=-=-=-=-=-=-=-=-')
def get_hole():
    return random.choice(Hole.objects.all())

def gen_fake_post(n = 100):
    post_pic = ['7054916.jpg','15400180.jpg','34497486.jpg']
    for i in range(n):
        Post.objects.create(user = get_user(),hole = get_hole(),
                            post = fakergen.paragraph(nb_sentences=30, variable_nb_sentences=True, ext_word_list=None),
                            title = fakergen.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
                            image = ['/post_pic/'+post_pic[random.randint(0,len(post_pic)-1)],''][random.randint(0,1)]
                            )
        if i%(n//10) == 0:
                print(str(i)+' completed')
    print('-=-=-=-=-=-=-=-=-=COMPLETED=-=-=-=-=-=-=-=-=-=-')

def get_post():
    return random.choice(Post.objects.exclude(reply_id = 0).all())
def gen_random_bool():
        return [True,True,False][random.randint(0,2)]
def gen_fake_votes(n = 100):
        print('-=-=-=-=-=-=-=-=-=GENERATING=-=-=-=-=-=-=-=-=-')
        print('0%')
        for i in range(n):
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
                if i%(n//10) == 0:
                        print(str(i)+' completed')
        print('-=-=-=-=-=-=-=-=-=COMPLETED=-=-=-=-=-=-=-=-=-=-')

def gen_fake_reply(n = 100):
        post_list = Post.objects.filter(reply_id = 0).order_by('creation_datetime')
        print('-=-=-=-=-=-=-=-=-=GENERATING=-=-=-=-=-=-=-=-=-')
        print('0%')
        for i in range(n):
                post = post_list[random.randint(0,len(post_list)-1)].pk
                user = get_user()
                hole = get_hole()
                reply = Post.objects.create(user = user,hole = hole,reply_id = post,post = fakergen.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None))
                if i%(n//10) == 0:
                        print(str(i)+' completed')
        print('-=-=-=-=-=-=-=-=-=COMPLETED=-=-=-=-=-=-=-=-=-=-')
def gen_fake_reply_reply(n=100):
        post_list = Post.objects.exclude(reply_id = 0).order_by('-creation_datetime')
        print('-=-=-=-=-=-=-=-=-=GENERATING=-=-=-=-=-=-=-=-=-')
        print('0%')
        for i in range(n):
                post = post_list[random.randint(0,len(post_list)-1)].pk
                user = get_user()
                hole = get_hole()
                reply = Post.objects.create(user = user,hole = hole,reply_id = post,post = fakergen.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None))
                if i%(n//10) == 0:
                        print(str(i)+' completed')
        print('-=-=-=-=-=-=-=-=-=COMPLETED=-=-=-=-=-=-=-=-=-=-')

def gen_fake_user(n=10):
        print('-=-=-=-=-=-=-=-=-=GENERATING=-=-=-=-=-=-=-=-=-')
        print('0%')
        for i in range(n):
                p = fakergen.simple_profile(sex=None)
                user = User(
                        first_name = p['name'].split(' ')[0],
                        last_name = p['name'].split(' ')[1],
                        username = p['username'],
                        email = p['mail']
                )
                # user.save()
                user.set_password('12345678')
                user.save()
                user_profile = UserPortfolio(
                        user = user,
                        portfolio_url = fakergen.url(schemes=None),
                        profile_pic = 'profile_pic/download.jpg'
                )
                user_profile.save()
                if i%(n//10) == 0:
                        print(str(i)+' completed')
        print('-=-=-=-=-=-=-=-=-=COMPLETED=-=-=-=-=-=-=-=-=-=-')