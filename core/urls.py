from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("record/add_record", views.add_record_view, name="add_record"),
    path("record/<int:pk>", views.record_view, name="record_detail"),
    path("record/<int:pk>/edit", views.edit_record_view, name="edit_record"),
    path("record/<int:pk>/delete", views.delete_record_view, name="delete_record"),
]