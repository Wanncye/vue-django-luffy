from rest_framework import serializers
from .models import Banner
from .models import Nav
class BannerModelSerializer(serializers.ModelSerializer):
    #字段声明

    """轮播广告的序列化器"""
    #模型序列化器字段声明
    class Meta:
        model = Banner
        # fileds = '__all__'
        fields = ['image_url', 'link']

    #验证方法

    #存储数据方法

class NavModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ['title', 'link', 'is_site']