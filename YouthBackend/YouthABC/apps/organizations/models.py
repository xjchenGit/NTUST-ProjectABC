# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
# Create your models here.

class CityDict(models.Model):
    """
    机构/老师所在城市
    """
    province_name = models.CharField(max_length=20, verbose_name="省份")
    city_name = models.CharField(max_length=20, verbose_name="城市")
    add_time = models.DateField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name

class CourseOrg(models.Model):
    """
    课程机构
    """
    city_name = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name="所在城市")
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    tag = models.CharField(default='全国知名', max_length=10, verbose_name='机构标签')
    category = models.CharField(default="pxjg", verbose_name="机构类别", max_length=20, choices=(("pxjg", "机构"), ("gr", "个人"), ("gx", "高校")))
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    course_nums = models.IntegerField(default=0, verbose_name="课程数")
    add_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    # # 获取课程机构的教师数量
    # def get_teacher_nums(self):
    #     return self.teacher_set.all().count()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    """
    老师信息
    """
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=18, verbose_name="年龄")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)
    add_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name