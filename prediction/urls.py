
from django.urls import path
from prediction.views import index, register, home
from prediction import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
