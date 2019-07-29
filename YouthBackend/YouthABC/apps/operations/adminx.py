import xadmin
from xadmin import views

from .models import Banner,UserAsk,CourseComments
from .models import UserFavorite,UserMessage


# Register your models here.

class CoursesAdmin(object):
    list_display = ['name', 'detail']
    search_fields = ['name']
    model_icon = 'fa fa-telegram'
    style_fields = {"detail":"ueditor"}


xadmin.site.register(Course, CoursesAdmin)
# Register your models here.
