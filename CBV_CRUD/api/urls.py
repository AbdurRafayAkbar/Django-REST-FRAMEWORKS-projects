from django.urls import path
from .views import StudentApi


urlpatterns = [
    path("students/",StudentApi.as_view(),name="students"),
    path("students/<int:pk>",StudentApi.as_view(),name="students_ids")
]
