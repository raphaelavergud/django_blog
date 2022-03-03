from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.get_blogposts),
    path("api/add/", views.add_blogposts),
]
