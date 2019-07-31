from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .serializers import CityDictSerializer,CourseOrgSerializer,TeacherSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import CityDict,CourseOrg,Teacher
# Create your views here.

class CityDictPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "city_page"
    max_page_size = 100

class CityDictViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    所有城市的列表（ViewSet）
    """
    queryset = CityDict.objects.all().order_by('id')
    serializer_class = CityDictSerializer

     # 分页
    pagination_class = CityDictPagination


class CourseOrgViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    所有课程机构的列表（ViewSet）
    """
    queryset = CourseOrg.objects.all().order_by('id')
    serializer_class = CourseOrgSerializer

class TeacherViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    所有老师的列表（ViewSet）
    """
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer