from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('create_hole',views.create_hole,name = 'create_hole'),
    path('create_post',views.create_post,name = 'create_post'),
    path('h/<slug:slug>',views.get_hole),
    path('temp',views.temp,name = 'temp'),
    # # path('login',views.user_login,name = 'login'),
]