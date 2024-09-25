from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('index/', views.homepage, name='index'),
        path('', views.home, name='home'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('sign_up/', views.sign_up, name='sign_up'),
        path('login/', views.user_login, name='login'),
        path('account/', views.user_account, name='user_account'),
        path('logout/', auth_views.LogoutView.as_view(next_page='/index/'), name='logout'),
        path('edexcel/', views.edexcel, name='edexcel'),
        path('igcse/', views.igcse, name='igcse'),
        path('844/', views.eight_four_four, name='eight_four_four')
        # path('confirm_email/<uidb64>/<token>/', views.confirm_email, name='confirm_email'),
        ]
