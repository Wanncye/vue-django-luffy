from rest_framework import serializers
from .models import User
import re
from .utils import get_user_by_account
from django.contrib.auth.hashers import make_password
class UserModelSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True, help_text="短信验证码")
    token = serializers.CharField(max_length=1024, read_only=True, help_text="token认证字符串")
    class Meta:
        model = User
        fields = ['id', 'username', 'token', 'mobile', 'sms_code', 'password']
        extra_kwargs = {
            "mobile":{
                "write_only": True,
            },
            "username":{
                "read_only": True,
            },
            "id":{
                "read_only": True,
            },
            "password":{
                "write_only": True,
            }
        }

    def validate(self, attrs):
        mobile = attrs.get("mobile")
        sms_code = attrs.get("sms_code")
        password = attrs.get("password")
        # 验证手机号码的格式
        if not re.match("^1[3-9]\d{9}", mobile):
            raise serializers.ValidationError("对不起，手机号码格式有误")

        # 验证手机号是否已经注册过
        ret = get_user_by_account(mobile)
        if ret is not None:
            raise serializers.ValidationError("对不起，手机已经被注册")

        # todo 验证短信验证码是否正确

        return attrs

    def create(self, validated_data):
        """保存用户信息"""
        validated_data.pop("sms_code") #移除掉不需要的数据
        #对密码进行加密
        raw_password = validated_data.get("password")
        hash_password = make_password(raw_password)
        #对用户名设置一个默认值
        username = validated_data.get("mobile")
        #调用序列化器提供的create方法
        # super().create()
        user = User.objects.create(
            mobile=username,
            username=username,
            password=hash_password,
        )

        from rest_framework_jwt.settings import api_settings
        # 使用restframework.jwt提供手动生成token的方法生成登录状态
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user