from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', index, name='index')
]