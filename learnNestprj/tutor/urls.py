from django.urls import path
from . import views

urlpatterns = [
        path('create_admin/', views.create_admin, name='create_admin'),
        path('dashboard/', views.admin_dashboard, name='custom-admin_dashboard'),
        path('admin_login/', views.login_view, name='admin_login'),
        path('admin_logout/', views.admin_logout, name='admin_logout'),

        path('create_tutor/', views.create_tutor, name='create_tutor'),
        path('tutor_created/', views.tutor_created, name='tutor_created'),
        path('tutor_login/', views.tutor_login, name='tutor_login'),
        path('reset_password/', views.reset_password, name='reset_password'),
        path('tutors_dashboard/', views.tutors_dashboard, name='tutors_dashboard'),
        path('custom_logout/', views.custom_logout, name='custom_logout'),
        path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
        path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
        ]
