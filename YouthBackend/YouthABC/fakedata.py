import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YouthABC.settings')

import django
django.setup()

from courses.models import CoursesCategory, Tag, Course, BannerCourse, Lesson, Video, CourseResource
from users.models import UserProfile, ChildrenProfile
from organizations.models import CityDict,CourseOrg,Teacher

from faker import Faker
import random

fakegen = Faker("zh_CN")
fake_n = ""

fake_ctgs3 = ["语文", "数学", "英语", "政治", "历史", "地理", "科学", "教育"]
fake_ctgs2 = ["初级", "中级", "高级"]
fake_ctgs = ["实战", "练习", "小测"]

fake_istab = ["False", "True"]
fake_code = fakegen.ean8()
fake_desc = fakegen.text(max_nb_chars=150)
fake_addtime = fakegen.date(pattern="%Y-%m-%d")

rand_ctgs3 = random.choice(fake_ctgs3) + str(fake_n)

fake_tag = fakegen.word()
#############################################fakedata of user##################
# fake_username = fakegen.user_name() 
# def fake_user(N=5):
#     for entry in range(N):
#         global fake_username
#         fake_username = fakegen.user_name()
#         fake_name = fakegen.name()
#         fake_phone = fakegen.phone_number()
#         fake_address = fakegen.address()
#         user_pro = UserProfile.objects.get_or_create(username=fake_username, nick_name = fake_name, parent_mobile = fake_phone, address = fake_address)
        
#         ##############childprofile############
#         a = UserProfile.objects.get(username=fake_username)
#         fake_stuname = fakegen.user_name()
#         fake_nick = fakegen.name()
#         fake_birth = fakegen.date(pattern="%Y-%m-%d")
#         fake_desc = fakegen.text(max_nb_chars=20)
#         fake_gender = random.choice(["male", "female"])
#         user_stu = ChildrenProfile.objects.create(child_username = fake_stuname, parent_name = a, child_nick = fake_nick, gender = fake_gender, birthday = fake_birth, personal_signature = fake_desc)



###################################fakedata of organizations################

# fake_province = fakegen.province()
# fake_city = fakegen.city()
# citydic = CityDict.objects.create(province_name = fake_province, city_name = fake_city)
# citydic_instance = CityDict.objects.get(city_name = fake_city)

# fake_orgcode = fakegen.ean8()
# fake_org = fakegen.company()

# fake_teach_username = fakegen.user_name()

def fake_citydic(N = 5):
    global fake_n
    for entry in range(N):
        intn = entry+4
        fake_n = str(intn)
        fake_province = fakegen.province()
        fake_city = fakegen.city()
        citydic = CityDict.objects.create(province_name = fake_province, city_name = fake_city)
        global citydic_instance 
        citydic_instance = CityDict.objects.get(city_name = fake_city)
        fake_courseorg()
        fake_taecher()

        fake_ctg()
        
        fake_course()
        intn = intn + 1


# def fake_courseorg():
#         global fake_orgcode
#         fake_orgcode = fakegen.ean8()
#         global fake_org
#         fake_org = fakegen.company()
#         fake_desc = fakegen.text(max_nb_chars=150)
#         fake_ctg = ["pxjg", "gr", "gx"]
#         rand_ctg = random.choice(fake_ctg)
#         fake_click = random.randint(1,1000)
#         fake_fav = random.randint(1,1000)
#         fake_addr = fakegen.address()
#         fake_stunum = random.randint(1,1000)
#         fake_course_nums = random.randint(1,600)
#         courseorg = CourseOrg.objects.create(org_code = fake_orgcode, city_name = citydic_instance, name = fake_org, 
#         desc = fake_desc, category = rand_ctg, click_nums = fake_click, fav_nums = fake_fav, 
#         address = fake_addr, students = fake_stunum, course_nums = fake_course_nums)

# def fake_taecher():
#         global fake_teach_username
#         fake_teach_username = fakegen.user_name()
#         fake_teachname = fakegen.name()
#         fake_years = random.randint(0,50)
#         fake_company = fakegen.company()
#         fake_position = fakegen.job()
#         fake_phone = fakegen.phone_number()
#         fake_click = random.randint(1,1000)
#         fake_fav = random.randint(1,1000)
#         fake_age = random.randint(10,100)
#         org_instance = CourseOrg.objects.get(org_code = fake_orgcode)
#         teacher = Teacher.objects.get_or_create(teach_user = fake_teach_username, org = org_instance, 
#         name = fake_teachname, work_years = fake_years, work_company = fake_org, work_position = fake_position, 
#         click_nums =fake_click, fav_nums =fake_fav, age = fake_age)




##############################fakedata of courses###############################
# fake_ctgs3 = ["语文", "数学", "英语", "政治", "历史", "地理", "科学", "教育"]
# fake_ctgs2 = ["初级", "中级", "高级"]
# fake_ctgs = ["实战", "练习", "小测"]

# fake_istab = ["False", "True"]
# fake_code = fakegen.ean8()
# fake_desc = fakegen.text(max_nb_chars=150)
# fake_addtime = fakegen.date(pattern="%Y-%m-%d")

# rand_ctgs3 = random.choice(fake_ctgs3) + str(fake_n)

# fake_tag = fakegen.job()

# def fake_ctg():
#         global fake_n
#         print(fake_n)
#         rand_ctgs = random.choice(fake_ctgs) + fake_n
#         rand_ctgs2 = random.choice(fake_ctgs2) + fake_n
#         global rand_ctgs3
#         rand_ctgs3 = random.choice(fake_ctgs3) + fake_n
#         rand_istab = random.choice(fake_istab)
#         fake_code = fakegen.ean8()
#         fake_desc = fakegen.text(max_nb_chars=150)
#         fake_addtime = fakegen.date(pattern="%Y-%m-%d")
#         ctg = CoursesCategory.objects.get_or_create(name = rand_ctgs, code = fake_code, desc = fake_desc, category_type = 1, is_tab = "False", add_time=fake_addtime)
#         fake_code = fakegen.ean8()
#         a = CoursesCategory.objects.get(name=rand_ctgs)
#         fake_desc = fakegen.text(max_nb_chars=150)
#         ctg2 = CoursesCategory.objects.get_or_create(name = rand_ctgs2, code = fake_code, desc = fake_desc, category_type = 2, parent_category =  a, is_tab = "False", add_time=fake_addtime)
#         fake_code = fakegen.ean8()
#         b = CoursesCategory.objects.get(name=rand_ctgs2)
#         fake_desc = fakegen.text(max_nb_chars=150)
#         ctg3 = CoursesCategory.objects.get_or_create(name = rand_ctgs3, code = fake_code, desc = fake_desc, category_type = 3, parent_category =  b, is_tab = rand_istab, add_time=fake_addtime)
        

# def fake_course():
#         fake_teacher = Teacher.objects.get(teach_user = fake_teach_username)
#         fakectg = CoursesCategory.objects.get(name = rand_ctgs3)
#         couseorg = CourseOrg.objects.get(name = fake_org)
#         fake_desc = fakegen.text(max_nb_chars=100)
#         fake_price = '%.2f' % random.uniform(0,10000)
#         global fake_ctgs2
#         fake_degree = random.choice(fake_ctgs2)
#         fake_istab = ["False", "True"]
#         global fake_tag
#         fake_tag = fakegen.word()
#         rand_istab = random.choice(fake_istab)
#         course = Course.objects.get_or_create(teacher = fake_teacher, category = fakectg, tag_name = fake_tag,
#         course_org = couseorg, name = rand_ctgs3, desc = fake_desc, shop_price = fake_price, 
#         learn_times = random.randint(0,500), degree = fake_degree, students = random.randint(0,500),
#         fav_nums = random.randint(0,5000), click_nums = random.randint(0,5000), notice = fakegen.text(max_nb_chars=100),
#         youneed_know = fakegen.text(max_nb_chars=200), detail = fakegen.text(max_nb_chars=200), is_banner = rand_istab)
#         fake_cou = Course.objects.get(tag_name = fake_tag)
#         the_tag = Tag.objects.get_or_create(course = fake_cou, tag = fake_tag)


# def fake_tags():
#         fake_course = rand_ctgs3
#         the_tag = Tag.objects.get_or_create(course = fake_cou, tag = fake_tag)

# def fake_course(N=5):
#     fake_ctgs3 = ["语文", "数学", "英语", "政治", "历史", "地理", "科学", "教育"]
#     fake_ctgs2 = ["初级", "中级", "高级"]
#     fake_ctgs = ["实战", "练习", "小测"]
    
#     for entry in range(N):
#         # fake_n = bytes(N)
#         #list1 = [ N ]
#         fake_n = str(N)
#         rand_ctgs = random.choice(fake_ctgs) + fake_n
#         rand_ctgs2 = random.choice(fake_ctgs2) + fake_n
#         rand_ctgs3 = random.choice(fake_ctgs3) + fake_n
#         fake_istab = ["False", "True"]
#         rand_istab = random.choice(fake_istab)
#         fake_code = fakegen.ean8()
#         fake_desc = fakegen.text(max_nb_chars=150)
#         fake_addtime = fakegen.date(pattern="%Y-%m-%d")
#         ctg = CoursesCategory.objects.get_or_create(name = rand_ctgs, code = fake_code, desc = fake_desc, category_type = 1, is_tab = "False", add_time=fake_addtime)
#         fake_code = fakegen.ean8()
#         fake_desc = fakegen.text(max_nb_chars=150)
#         ctg2 = CoursesCategory.objects.get_or_create(name = rand_ctgs2, code = fake_code, desc = fake_desc, category_type = 2, parent_category =  rand_ctgs, is_tab = "False", add_time=fake_addtime)
#         fake_code = fakegen.ean8()
#         fake_desc = fakegen.text(max_nb_chars=150)
#         ctg3 = CoursesCategory.objects.get_or_create(name = rand_ctgs3, code = fake_code, desc = fake_desc, category_type = 3, parent_category =  rand_ctgs2, is_tab = rand_istab, add_time=fake_addtime)


if __name__ == '__main__':
    print("data is loading")
    #fake_ctg(10)
    #fake_user(10)
    #fake_tags()
    #fake_citydic(10)
    print("done")

