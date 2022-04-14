from django.urls import path
from . import views
urlpatterns = [
    path(r'banner/', views.BannerListAPIView.as_view()),
]