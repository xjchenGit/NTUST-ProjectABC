import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YouthABC.settings')

import django
django.setup()

from courses.models import CoursesCategory, Tag, Course, BannerCourse, Lesson, Video, CourseResource
from faker import Faker
import random

fakegen = Faker("zh_CN")

def fake_ctg(N=5):

    fake_ctgs3 = ["语文", 
                  "数学", 
                  "英语", 
                  "政治", 
                  "历史", 
                  "地理", 
                  "科学",
                  "教育"]
    fake_ctgs2 = ["初级", "中级", "高级"]
    fake_ctgs = ["实战", "练习", "小测"]
    ctg = [{"name": "分类","code": "fx","sub_cat": "分类二"}]

    for ctg in 
        print(ctg)

if __name__ == '__main__':
    print("data is loading")
    # makefakedata(20)
    fake_ctg(10)
    
    print("done")