from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('news/', views.news, name='news'),
    path('register/', views.register, name='register'),
]