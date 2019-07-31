from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .serializers import CoursesCategorySerializer,TagSerializer,CourseSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import CoursesCategory,Tag,Course
from .models import BannerCourse

# Create your views here.

class CoursePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "courses_page"
    max_page_size = 100

class CourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    所有课程的列表（ViewSet）
    """
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer

     # 分页
    pagination_class = CoursePagination