import xadmin
from xadmin import views

from .models import UserProfile,ChildrenProfile
# Register your models here.


class UserProfileAdmin(object):
    list_display = ['nick_name', 'parent_mobile', 'image', 'address','add_time']
    search_fields = ['nick_name']
    model_icon = 'fa fa-telegram'

class ChildrenProfileAdmin(object):
    list_display = ['student_name', 'child_username', 'gender', 'birthday','school','current_grade','personal_signature']
    search_fields = ['student_name', 'child_username', 'gender', 'birthday','school','current_grade','personal_signature']
    model_icon = 'fa fa-telegram'

xadmin.site.register(ChildrenProfile, ChildrenProfileAdmin)