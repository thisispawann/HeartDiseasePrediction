
from django.urls import path
from prediction.views import index

urlpatterns = [
    path('', index, name='index'),
    
]
