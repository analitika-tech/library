from django.urls import path

from .views import BookGPView, BookPDView, StudentGPView, StudentPDView
from .views import IssueGPView, IssuePDView, ReservationGPView, ReservationPDView


urlpatterns = [
    # Book view's
    path("book/", BookGPView.as_view(), name = "book-view"),
    path("book/actions/<int:pk>", BookPDView.as_view(), name = "book-actions-view"),

    # Student view's
    path("student/", StudentGPView.as_view(), name = "student-view"),
    path("student/actions/<int:pk>", StudentPDView.as_view(), name = "student-actions-view"),

    # Issue view's
    path("issue/", IssueGPView.as_view(), name = "issue-view"),
    path("issue/actions/<int:pk>", IssuePDView.as_view(), name = "issue-actions-view"),

    # Issue view's
    path("reservation/", ReservationGPView.as_view(), name = "reservation-view"),
    path("reservation/actions/<int:pk>", ReservationPDView.as_view(), name = "reservation-actions-view"),
]
