import xadmin
from xadmin import views

from .models import OrderInfo,OrderCourses

# Register your models here.

class OrderInfoAdmin(object):
    list_display = ['user', 'order_sn', 'trade_no','pay_status','post_script','order_mount','pay_time']
    search_fields = ['user', 'order_sn','trade_no']
    list_filter = ['add_time']
    model_icon = 'fa fa-telegram'
    readonly_fields=['user', 'order_sn', 'trade_no','pay_status','post_script','order_mount','pay_time','add_time']

class OrderCoursesAdmin(object):
    list_display = ['order','courses','courses_num']
    search_fields = ['courses','courses_num']
    list_filter = ['add_time']
    model_icon = 'fa fa-telegram'

xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderCourses, OrderCoursesAdmin)
