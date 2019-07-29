import xadmin
from xadmin import views

from .models import Banner,UserAsk,CourseComments
from .models import UserFavorite,UserMessage,UserCourse


# Register your models here.

class BannerAdmin(object):
    list_display = ['title', 'image','url','index']
    search_fields = ['title']
    model_icon = 'fa fa-telegram'

class UserAskAdmin(object):
    list_display = ['name','mobile','course_name']
    search_fields = ['name']
    model_icon = 'fa fa-telegram'

class CourseCommentsAdmin(object):
    list_display = ['user','course','comments']
    search_fields = ['user','course','comments']
    model_icon = 'fa fa-telegram'

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
# Register your models here.
