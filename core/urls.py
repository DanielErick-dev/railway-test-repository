from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from .views import criar_superusuario_secreto


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("students/", include('students.urls')),
    path('super_usuario/', criar_superusuario_secreto, name='super_usuario')
]
