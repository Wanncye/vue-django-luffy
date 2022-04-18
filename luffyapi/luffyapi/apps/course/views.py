from rest_framework.generics import ListAPIView
from yaml import serialize_all
from .models import CourseCategory
from .serializers import CourseCategoryModelSerializer
class CourseCategoryListAPIView(ListAPIView):
    """
    课程分类
    """
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")
    serializer_class = CourseCategoryModelSerializer


# from .models import Course
# from .serializers import CourseModelSerializer
# class CourseListAPIView(ListAPIView):
#     """
#     课程信息
#     """
#     queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")
#     serializer_class = CourseModelSerializer

from .models import Course
from .serializers import CourseModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
class CourseListAPIView(ListAPIView):
    """
    课程信息
    """
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('course_category', )