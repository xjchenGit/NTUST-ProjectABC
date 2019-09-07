import xadmin
from xadmin import views

from .models import UserAsk,CourseComments

# Register your models here.

class UserAskAdmin(object):
    list_display = ['name', 'course_name']
    search_fields = ['name']
    model_icon = 'fa fa-telegram'

class CourseCommentsAdmin(object):
    list_display = ['user', 'course','comments']
    search_fields = ['course','comments']
    model_icon = 'fa fa-telegram'

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
# Register your models here.
