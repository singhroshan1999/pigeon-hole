"""MLForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authentication import views
import forum.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', forum.views.index,name = 'index'),
    path('auth/',include('authentication.urls')),
    # path('register/', views.register),
    # path('loginnn/', views.user_login,name = 'loginnn'),
    # path('logoutttt/', views.user_logout,name = 'logoutttt'),
    path('forum/', include('forum.urls')),
    # path('create_hole/', forum.views.create_hole,name = 'create_hole'),
    # path('create_post/', forum.views.create_post,name = 'create_post'),
]
