from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BookAPIView, ClassAPIView, StudentAPIView

urlpatterns = [
    path("bookapi/", BookAPIView.as_view(), name = "bookapi"),
    path("classapi/", ClassAPIView.as_view(), name = "classapi"),
    path("studentapi/", StudentAPIView.as_view(), name = "studentapi"),
]

urlpatterns = format_suffix_patterns(urlpatterns)