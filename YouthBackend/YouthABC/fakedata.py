import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YouthABC.settings')

import django
django.setup()

from courses.models import CoursesCategory, Tag, Course, BannerCourse, Lesson, Video, CourseResource
from faker import Faker
import random

fakegen = Faker("zh_CN")

def fake_ctg(N=5):
    fake_ctgs3 = ["语文", "数学", "英语", "政治", "历史", "地理", "科学", "教育"]
    fake_ctgs2 = ["初级", "中级", "高级"]
    fake_ctgs = ["实战", "练习", "小测"]
    
    for entry in range(N):
        # fake_n = bytes(N)
        #list1 = [ N ]
        fake_n = str(N)
        rand_ctgs = random.choice(fake_ctgs)
        rand_ctgs2 = random.choice(fake_ctgs2)
        rand_ctgs3 = random.choice(fake_ctgs3)
        fake_istab = ["False", "True"]
        rand_istab = random.choice(fake_istab)
        fake_addtime = fakegen.date(pattern="%Y-%m-%d")
        fake_code = fakegen.ean8()
        fake_desc = fakegen.text(max_nb_chars=150)
        ctg = CoursesCategory.objects.get_or_create(name = rand_ctgs + fake_n, code = fake_code, desc = fake_desc, category_type = 1, parent_category =  rand_ctgs+ fake_n, is_tab = "False", add_time=fake_addtime)
        
        ctg2 = CoursesCategory.objects.get_or_create(name = rand_ctgs2 + fake_n, code = fake_code, desc = fake_desc, category_type = 2, parent_category =  rand_ctgs, is_tab = "False", add_time=fake_addtime)
        
        ctg3 = CoursesCategory.objects.get_or_create(name = rand_ctgs3 + fake_n, code = fake_code, desc = fake_desc, category_type = 3, parent_category =  rand_ctgs2, is_tab = rand_istab, add_time=fake_addtime)


# def makefakedata(N=10):
#     for entry in range(N):
#         fake_tag = fakegen.job()
#         fake_time = fakegen.date(pattern="%Y-%m-%d")
#         tag = Tag.objects.get_or_create(name=fake_tag, add_time=fake_time)

if __name__ == '__main__':
    print("data is loading")
    # makefakedata(20)
    fake_ctg(10)
    print("done")

