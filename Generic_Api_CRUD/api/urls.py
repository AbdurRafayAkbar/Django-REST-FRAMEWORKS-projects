from .views import AllStudentAPI,SingleStudentApi
from django.urls import path

urlpatterns = [
    path("students/",AllStudentAPI.as_view()),
    path("students/<int:id>/",SingleStudentApi.as_view())
    
]
