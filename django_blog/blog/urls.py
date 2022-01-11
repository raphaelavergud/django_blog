from django.urls import path

from . import views

# first argument in urlpatterns is the path and second argument is which function that should be called from views for that path

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<int:id>/", views.blog_post, name="blog_post"),
    path("run/<int:id>/", views.run_log, name="run_log"),
    path("update_server/", views.update, name="update"),
    path("item/<item_id>/", views.item),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]

