from django.urls import path
from . import views
urlpatterns = [
    path(r'banner/', views.BannerListAPIView.as_view()),
    path(r'nav/header/', views.HeaderNavListAPIView.as_view()),
    path(r'nav/footer/', views.FooterNavListAPIView.as_view()),
]