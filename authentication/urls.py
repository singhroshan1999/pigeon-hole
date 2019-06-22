from django.urls import path
from authentication import views

app_name = 'auth'

urlpatterns = [
    path('',views.user_login,name = 'index'),
    path('login',views.user_login,name = 'login'),
    path('register',views.register,name = 'register'),
    path('logout',views.user_logout,name = 'logout'),
    # path('login',views.user_login,name = 'login'),
]