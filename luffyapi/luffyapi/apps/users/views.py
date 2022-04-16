# Create your views here.
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer
class UserAPIView(CreateAPIView):
    """用户信息视图"""
    #这里的queryset可加可不加
    queryset = User.objects.all()
    serializer_class = UserModelSerializer