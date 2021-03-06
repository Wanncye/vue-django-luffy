from email.policy import default
from django.db import models

class BaseModel(models.Model):
    """公共模型"""
    is_show = models.BooleanField(default=True,verbose_name="是否显示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        abstract = True