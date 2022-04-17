# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import User
from .serializers import UserModelSerializer
from .utils import get_user_by_account
from rest_framework.response import Response
from luffyapi.settings import constants
class UserAPIView(CreateAPIView):
    """用户信息视图"""
    #这里的queryset可加可不加
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

"""
GET /user/mobile/<mobile>/
"""
import re
from rest_framework import status
class MobileAPIView(APIView):
    def get(self,request,mobile):
        ret = get_user_by_account(mobile)
        if ret is not None:
            return Response({"message":"手机号已经被注册过！"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"ok"})

import random
from django_redis import get_redis_connection
from luffyapi.libs.yuntongxun.sms import CCP
class SMSAPIView(APIView):
    def get(self, request, mobile):
        """短信发送接口"""
        #1. 判断手机号码有没有在60秒内重复发送请求
        redis_conn = get_redis_connection("sms_code")
        ret = redis_conn.get("mobile_%s" % mobile)
        if ret is not None:
            return Response({"message" : "对不起，短信60秒内已经发送，请耐心等待"})
        
        #2.. 生成短信验证码
        sms_code = "06%d" % random.randint(100000,999999)

        #3. 保存验证码到redis
        redis_conn.setex("sms_%s" % mobile, constants.SMS_EXPIRE_TIME, sms_code)
        redis_conn.setex("mobile_%s" % mobile, constants.SMS_INTERVAL, "_")

        #4. 调用短信sdk接口，发送短信
        try:
            ccp = CCP()
            ret = ccp.send_template_sms(mobile, [sms_code, constants.SMS_EXPIRE_TIME//60], constants.SMS_TEMPLATE_ID)
        except:
            return Response({"message" : "发送短信失败"})

        #5. 相应发送短信的结果
        return  Response({"message" : "发送短信成功"})
