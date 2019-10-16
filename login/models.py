from django.db import models


# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
)

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")  # 使用choices,选择男女,default默认为男
    c_time = models.DateTimeField(auto_now_add=True)    # auto_mow_add 显示创建时间
    has_confirmed = models.BooleanField(default=False)  # 增加是否邮件确认字段

    # 重新str方法,人性化的显示用户姓名
    def __str__(self):
        return self.name

    # 元数据,定义排序方法 按创建时间倒叙
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    # 元数据 定义排序方法
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
