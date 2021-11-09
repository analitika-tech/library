from django.urls import path
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BookAPIView, ClassAPIView, StudentAPIView

urlpatterns = [
    path("bookapi/", login_required(BookAPIView.as_view()), name = "bookapi"),
    path("classapi/", login_required(ClassAPIView.as_view()), name = "classapi"),
    path("studentapi/", login_required(StudentAPIView.as_view()), name = "studentapi"),
]

urlpatterns = format_suffix_patterns(urlpatterns)