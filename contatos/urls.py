from django.urls import path
from . import views

urlpatterns = [
    path('', views.contato_list, name='contato_list'),
]