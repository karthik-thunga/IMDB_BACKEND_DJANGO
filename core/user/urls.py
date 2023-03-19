from rest_framework.authtoken.views import  obtain_auth_token
from core.user.views import register_user, logout
from django.urls import path

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout, name='register'),

]