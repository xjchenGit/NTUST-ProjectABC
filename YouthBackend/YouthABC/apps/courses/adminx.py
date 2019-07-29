import xadmin
from xadmin import views

from .models import Course,Tag,CoursesCategory,BannerCourse
from .models import Lesson,Video,CourseResource
# Register your models here.

class CoursesAdmin(object):
    list_display = ['name', 'detail']
    search_fields = ['name']
    model_icon = 'fa fa-telegram'
    style_fields = {"detail":"ueditor"}

class CoursesCategoryAdmin(object):
    list_display = ['name','category_type','parent_category']
    search_fields = ['name']
    model_icon = 'fa fa-telegram'

class BannerCourseAdmin(object):
    list_display = ['name', 'detail']
    search_fields = ['name']
    model_icon = 'fa fa-telegram'

class TagAdmin(object):
    list_display = ['name']
    model_icon = 'fa fa-telegram'
    
class LessonAdmin(object):
    list_display = ['course','name','learn_times']
    model_icon = 'fa fa-telegram'

class VideoAdmin(object):
    list_display = ['lesson','name','learn_times','url']
    model_icon = 'fa fa-telegram'

class CourseResourceAdmin(object):
    list_display = ['course','name']
    model_icon = 'fa fa-telegram'


xadmin.site.register(Course, CoursesAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(CoursesCategory, CoursesCategoryAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
