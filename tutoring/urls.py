from django.urls import path

from .views import TutoringListView

urlpatterns = [
    path("tutorias/", TutoringListView.as_view(), name="tutorias"),
]
