
from django.urls import path
from prediction.views import index, register, home, result, starter
from prediction import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', starter, name='starter'),
    path('index/', index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('result/', result, name='result')
]
