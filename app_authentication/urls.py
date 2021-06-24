from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/signup/',views.user_signup, name='signup'),
    path('api/v1/login/',views.user_login, name='login')
]
