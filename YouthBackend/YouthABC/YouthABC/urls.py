"""YouthABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from __future__ import unicode_literals
import xadmin
# from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from YouthABC.settings import MEDIA_ROOT

#APIurl部分
from rest_framework.documentation import include_docs_urls
from organizations.views import CityDictViewSet,CourseOrgViewSet,TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#配置CityDict的url
router.register('citydict', CityDictViewSet,base_name="citydict")

#配置CourseOrg的url
router.register('courseorg', CourseOrgViewSet,base_name="courseorg")

#配置Teacher的url
router.register('teacher', TeacherViewSet,base_name="teacher")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    re_path('media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    #include router
    re_path('^', include(router.urls)),
    #drf文档，title自定义
    path('docs',include_docs_urls(title='智富ABC——API文档')),
    
]


