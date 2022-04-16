from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns = [
    path(r'login/', obtain_jwt_token),
    path(r'reg/', views.UserAPIView.as_view()),
]