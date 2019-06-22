from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('create_hole',views.create_hole,name = 'create_hole'),
    path('create_post',views.create_post,name = 'create_post'),
    # path('logout',views.user_logout,name = 'logout'),
    # # path('login',views.user_login,name = 'login'),
]