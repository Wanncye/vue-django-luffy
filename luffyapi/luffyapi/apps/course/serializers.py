from rest_framework import serializers
from .models import CourseCategory
class CourseCategoryModelSerializer(serializers.ModelSerializer):
    """
    课程分类序列化器
    """
    class Meta:
        model = CourseCategory
        fields = ["id", "name"]

from .models import Teacher
class TeacherModelSerializer(serializers.ModelSerializer):
    """
    老师序列化器
    """
    class Meta:
        model = Teacher
        fields = ['id', 'title', 'name', 'signature', 'image', 'brief']



from .models import Course
class CourseModelSerializer(serializers.ModelSerializer):
    """
    课程信息序列化器
    """
    #序列化器嵌套，返回外键对应的序列化器值，必须是外键
    teacher = TeacherModelSerializer()
    class Meta:
        model = Course
        fields = ["id","name","students","lessons","pub_lessons","price","course_img","teacher","lesson_list"]

class CourseRetrieveModelSerializer(serializers.ModelSerializer):
    """
    详情页课程信息序列化器
    """
    teacher = TeacherModelSerializer()
    class Meta:
        model = Course
        fields = ["id","name","students","lessons","pub_lessons","price","course_img","teacher","level_name","brief_html","course_video"]
