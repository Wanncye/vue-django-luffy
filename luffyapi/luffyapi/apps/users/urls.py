from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns = [
    path(r'login/', obtain_jwt_token),
    path(r'reg/', views.UserAPIView.as_view()),
    re_path(r"mobile/(?P<mobile>1[3-9]\d{9})/", views.MobileAPIView.as_view()),
]