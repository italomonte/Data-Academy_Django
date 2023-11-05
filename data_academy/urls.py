from django.urls import path
from . import views

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('content/', views.content, name="content"),
    path('login/', views.login, name="login"),
    path('interpretador/', views.interpretador, name='interpretador')
]