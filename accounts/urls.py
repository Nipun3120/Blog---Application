from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('signup/', views.signupView, name='signup'),
]