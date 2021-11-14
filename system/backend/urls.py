from django.urls import path
from django.contrib.auth.decorators import login_required

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from .views import BookAPIView, ClassAPIView, StudentAPIView

urlpatterns = [
    path("bookapi/", login_required(BookAPIView.as_view()), name = "bookapi"),
    path("classapi/", login_required(ClassAPIView.as_view()), name = "classapi"),
    path("studentapi/", login_required(StudentAPIView.as_view()), name = "studentapi"),
    path("api-documentation/", include_docs_urls(title = "API's", public = False), name = "api-docs"),
    path('schema/', get_schema_view(
        title="Library managemnt Software API Schema",
        description="API Schema for all API endpoints in our Web App",
        version="0.0.1"
    ), name='api-schema'),
]

urlpatterns = format_suffix_patterns(urlpatterns)