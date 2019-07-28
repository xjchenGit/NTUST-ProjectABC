from rest_framework import serializers
from .models import CityDict,CourseOrg,Teacher

class CityDictSerializer(serializers.ModelSerializer):
    """
    所有城市列表
    """
    class Meta:
        model = CityDict
        fields = "__all__"

class CourseOrgSerializer(serializers.ModelSerializer):
    """
    所有课程机构的列表
    """
    class Meta:
        model = CourseOrg
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    """
    所有课程机构的列表
    """
    class Meta:
        model = Teacher
        fields = "__all__"