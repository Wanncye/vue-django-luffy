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

#分页器是放在列表视图中的
from rest_framework.pagination import PageNumberPagination
class CoursePageNumberPagination(PageNumberPagination):
    """课程列表的分页器"""
    page_query_param = "page" # 地址上面代表页码的变量名，默认为page
    page_size = 2  # 每一页显示的数据量，默认是10条， 没有设置页码，则不进行分页
    # 允许客户端通过指定的参数名来设置每一页数据量的大小，默认是size
    page_size_query_param = "size"
    max_page_size = 20  # 限制每一页最大展示的数据量

from .models import Course
from .serializers import CourseModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class CourseListAPIView(ListAPIView):
    """
    课程信息
    """
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ('course_category', )
    ordering_fields = ('id', 'students', 'price', )
    pagination_class = CoursePageNumberPagination

from rest_framework.generics import RetrieveAPIView
from .serializers import CourseRetrieveModelSerializer
class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders","-id")
    serializer_class = CourseRetrieveModelSerializer

from .models import CourseChapter
from .serializers import CourseChapterModelSerializer
class CourseChapterListAPIView(ListAPIView):
    queryset = CourseChapter.objects.filter(is_show=True, is_delete=False).order_by("orders","id")
    serializer_class = CourseChapterModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']