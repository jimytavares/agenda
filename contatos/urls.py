from django.urls import path
from . import views

urlpatterns = [
    path('', views.contato_list, name='contato_list'),
    path('contato_add/', views.contato_add, name='contato_add'),
    path('contato_edit/<int:pk>', views.contato_edit, name='contato_edit'),
    path('contato_del/<int:pk>', views.contato_del, name='contato_del')
]