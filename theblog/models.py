from django.db import models
# 导入之前创建的超级用户
from django.contrib.auth.models import User

# Create your models here.

# 博文
class Post(models.Model):
    # 标题
    title = models.CharField(max_length=255)
    # 作者就是超级用户
    # 如果我们删除了超级用户
    # 与之相连接的所有文章都会被删除
    # 注意这里使用的是外键进行连接
    # 后面的 CASCADE 是必须要有的
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # 文章内容
    body = models.TextField()

    def __str__(self):
        # 这将使得我们在后端管理页面看到这些返回的内容
        # 但如果我们想要对其能进行管理
        # 还需要在 admin。py 文件中进行注册
        # 注意这里的 self.author 必须转换为 字符串 否则后端无法进行展示会报错
        return self.title +' | '+ str(self.author)