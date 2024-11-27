from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path('registration/', views.register_user, name='register'),
    path('registration/', views.RegistrationView.as_view(), name='register'),
    # path('logout/', views.logout_user, name='logout')
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginUserView.as_view(), name='login')
]
