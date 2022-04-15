from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from .models import Banner
from .serializers import BannerModelSerializer
from luffyapi.settings import constants

class BannerListAPIView(ListAPIView):
    """轮播广告视图"""
    #query相当于数据库里面的select操作
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders","-id")[:constants.BANNER_LENGTH]
    #序列化器，只显示序列化器中fields字段
    serializer_class = BannerModelSerializer

