from django.contrib import admin
from forum.models import Hole,Post,HoleFollower

# Register your models here.
admin.site.register(Hole)
admin.site.register(Post)
admin.site.register(HoleFollower)