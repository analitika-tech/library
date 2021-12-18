from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

from .views import BookGPView, BookPDView, ClassGPView, ClassPDView, StudentGPView, StudentPDView
from .views import ReservationGPView, ReservationPDView, IssueGPView, IssuePDView
from .views import home_view, error_view, tutorial_view, login_view, logout_view, parser_view

urlpatterns = [
    # Home view
    path("", home_view, name = "home-view"),

    # Error view
    path("error/", error_view, name = "error-view"),

    # Tutorial view
    path("tutorial/", tutorial_view, name = "tutorial-view"),

    # Parser
    path("parser/", parser_view, name = "parser-view"),

    # Book view's
    path("book/", login_required(BookGPView.as_view()), name = "book-view"),
    path("book/actions/<int:pk>", login_required(BookPDView.as_view()), name = "book-actions-view"),

    # Class view's
    path("class/", login_required(ClassGPView.as_view()), name = "class-view"),
    path("class/actions/<int:pk>", login_required(ClassPDView.as_view()), name = "class-actions-view"),

    # Student view's
    path("student/", login_required(StudentGPView.as_view()), name = "student-view"),
    path("student/actions/<int:pk>", login_required(StudentPDView.as_view()), name = "student-actions-view"),

    # Issue view's
    path("reservation/", login_required(ReservationGPView.as_view()), name = "reservation-view"),
    path("reservation/actions/<int:pk>", login_required(ReservationPDView.as_view()), name = "reservation-actions-view"),
    
    # Issue view's
    path("issue/", login_required(IssueGPView.as_view()), name = "issue-view"),
    path("issue/actions/<int:pk>", login_required(IssuePDView.as_view()), name = "issue-actions-view"),

    # Authentication view's
    path("login/",login_view ,name = "login-view"),
    path("logout/", logout_view ,name = "logout-view")

]