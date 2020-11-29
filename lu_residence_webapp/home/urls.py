from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('news/', views.news, name='news'),
    path('faq/', views.faq, name='faq'),
    path('register/', views.register, name='register'),
    path('housing/', views.housing, name='housing'),
]