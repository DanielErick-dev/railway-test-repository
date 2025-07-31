from django.contrib import admin
from django.urls import path
from django.contrib.auth import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
]
