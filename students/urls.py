from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.GetStudents.as_view(), name='get_students'),
    path("create/", views.CreateStudents.as_view(), name='create_students'),
    path("detail/<int:pk>/", views.DetailStudents.as_view(), name='detail_students'),
    path("delete/<int:pk>/", views.DeleteStudents.as_view(), name='delete_students'),
    path("update/<int:pk>/", views.UpdateStudents.as_view(), name='update_students'),
    path("atualize/<int:pk>/", views.atualize_students, name='atualize_students'),
    path("pending/", views.GetPendingStudents.as_view(), name='pending_students'),
    path("inactive/", views.GetInactiveStudents.as_view(), name='inactive_students')
]
