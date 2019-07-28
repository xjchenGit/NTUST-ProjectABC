#将下一个版本的部分新特性注入到当前版本
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# auth_user里面有id、password、last_login、is_superuser、username、first_name、last_name
# email、is_staff、is_active、datejoined
class UserProfile(AbstractUser):
    """
    用户信息
    """
    #家长信息
    nick_name = models.CharField(max_length=50,verbose_name="昵称")
    image = models.ImageField(upload_to="image/%Y/%m",verbose_name="头像",default="image/default.png", max_length=100)
    parent_mobile = models.CharField(max_length=11,verbose_name="家长手机号",null=True, blank=True)
    address = models.CharField(max_length=100,verbose_name="收货地址管理")
    
    #孩子信息
    student_name = models.CharField(max_length=50,verbose_name="学员姓名")
    gender = models.CharField(max_length=50, choices=(("male", "男"), ("female", "女")), default="female")
    birthday = models.DateField(verbose_name="出生年月", null=True, blank=True)
    school = models.CharField(max_length=50,verbose_name="所在学校",default="学校")
    current_grade = models.CharField(max_length=50,verbose_name="所在年级",default="一年级")
    personal_signature = models.CharField(max_length=50,verbose_name="个性签名",default=" ")
    
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username

