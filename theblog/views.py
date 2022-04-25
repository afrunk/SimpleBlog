from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from .models import Post
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

# 传递model 的数据给首页
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

# 传递博文的详情给具体的内容
class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'articles_detail.html'