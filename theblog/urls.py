from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView

urlpatterns = [
    # path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'), # 首页
    # pk是属于每个博文的键 即博文在数据库中的主键
    # {% url 'article_detail' post.pk %} 这是在 a 标签中填充的内容
    # post.pk 在 for 中遍历可以获取到的 ，而这样子也实现了不同的内容不同的路由
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_detail'),
]
