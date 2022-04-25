from django.contrib import admin
from .models import Post
# Register your models here.

# 注册model 这样子才能在admin 页面进行查看
admin.site.register(Post)