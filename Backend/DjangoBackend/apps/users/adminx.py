__author__='言简'

import xadmin
from xadmin import views
from .models import VerifyCode

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '言简在线学习'
    site_footer = "www.baidu.com"

class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
# xadmin.site.register(views.BaseAdminView,BaseSetting)
# xadmin.site.register(views.CommAdminView,GlobalSettings)