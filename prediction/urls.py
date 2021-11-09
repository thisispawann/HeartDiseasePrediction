
from django.urls import path
from prediction.views import index, register
from prediction import views

urlpatterns = [
    path('', index, name='index'),
    path('register/', views.register, name='register'),
]
