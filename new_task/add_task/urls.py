from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('home/', views.home, name='home'), 
    path('form/', views.form_view, name='form_view'), 
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'), 
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'), 
]
