from django.urls import path

from .views import BookGPView, BookPDView

urlpatterns = [
    # Book view's
    path("book/", BookGPView.as_view(), name = "book-view"),
    path("book/actions/<int:pk>", BookPDView.as_view(), name = "book-actions-view"),
]