import xadmin
from xadmin import views

from .models import CityDict, CourseOrg, Teacher
# Register your models here.


class CityDictAdmin(object):
    list_display = ['province_name', 'city_name', 'add_time']
    search_fields = ['province_name', 'city_name']
    list_filter = ['province_name', 'add_time']
    model_icon = 'fa fa-telegram'

class CourseOrgAdmin(object):
    list_display = ['name','desc']
    search_fields = ['name']
    list_filter = ['name']
    model_icon = 'fa fa-telegram'

class TeacherAdmin(object):
    list_display = ['name','org','image']
    search_fields = ['org', 'name']
    list_filter = ['org', 'name']
    model_icon = 'fa fa-telegram'

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
