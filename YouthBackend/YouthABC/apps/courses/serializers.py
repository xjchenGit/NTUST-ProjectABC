from rest_framework import serializers
from .models import CoursesCategory,Tag,Course,Lesson,Video,CourseResource
from .models import BannerCourse

class CoursesCategorySerializer(serializers.ModelSerializer):
    """
    所有课程类别
    """
    class Meta:
        model = CoursesCategory
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    """
    所有标签
    """
    class Meta:
        model = Tag
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    """
    所有课程列表
    """
    class Meta:
        model = Course
        fields = "__all__"
