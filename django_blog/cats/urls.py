from django.urls import path

from . import views

# first argument in urlpatterns is the path and second argument is which function that should be called from views for that path

urlpatterns = [
    path("cats/", views.CatView, name="CatView"),
    path("cats/<str:cat_text>", views.CatPic, name="CatPic"),
]
