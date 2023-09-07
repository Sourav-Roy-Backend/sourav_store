from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='registerpage'),
    path('login/',views.user_login, name='loginpage'),
    path('profile/',views.profile, name='profilepage'),
    path('logout/',views.user_logout, name='logoutpage'),
    
]

