from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('user/', views.user_home, name='user_home'),
    path('form/', views.userform_view, name='userform_view'),
    path('change-password/', views.change_password, name='change_password'),
    path('edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('delete/<int:user_id>/', views.user_delete, name='user_delete'),
    
]
