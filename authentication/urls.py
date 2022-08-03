from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
  path('', views.signin, name='signin'),
  path('<str:error>', views.signin, name='signin'),
  path('signup/', views.signup, name='signup'),
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
]