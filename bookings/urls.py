from django.urls import path

from .views import BookingCreateView, BookingUpdateView

urlpatterns = [
    path("solicitar/", BookingCreateView.as_view()),
    path("solicitud/<int:pk>/", BookingUpdateView.as_view()),
]
