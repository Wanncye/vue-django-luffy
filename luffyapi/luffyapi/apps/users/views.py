# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import User
from .serializers import UserModelSerializer
from .utils import get_user_by_account
from rest_framework.response import Response

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