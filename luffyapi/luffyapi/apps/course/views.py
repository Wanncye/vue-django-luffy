from rest_framework.generics import ListAPIView
from yaml import serialize_all
from .models import CourseCategory
from .serializers import CourseCategoryModelSerializer
class CourseCategoryListAPIView(ListAPIView):
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")
    serializer_class = CourseCategoryModelSerializer
