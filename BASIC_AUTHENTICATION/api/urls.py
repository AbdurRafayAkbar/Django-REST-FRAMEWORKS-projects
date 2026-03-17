from django.urls import path
from . import views

urlpatterns = [
    path("public_view/",views.public_view,name="public_view"),
    path("private_view/",views.private_view,name="private_view")
]
