from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout')
]
