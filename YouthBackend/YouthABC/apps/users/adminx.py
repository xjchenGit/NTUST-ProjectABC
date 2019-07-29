import xadmin
from xadmin import views

from .models import UserProfile,ChildrenProfile
# Register your models here.


class UserProfileAdmin(object):
    list_display = ['nick_name', 'city_name', 'add_time']
    search_fields = ['province_name', 'city_name']
    model_icon = 'fa fa-telegram'

xadmin.site.register(CityDict, CityDictAdmin)