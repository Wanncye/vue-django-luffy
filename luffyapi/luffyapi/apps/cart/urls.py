from django.urls import path,re_path
from . import views
urlpatterns = [
    path(r"", views.CartAPIView.as_view({"post":"add","get":"list","patch":"change_selected"}) ),
]