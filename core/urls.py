from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("record/<int:pk>", views.record_view, name="record_detail"),
]