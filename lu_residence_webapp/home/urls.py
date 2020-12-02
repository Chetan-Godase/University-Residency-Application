from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('news/', views.news, name='news'),
    path('apply/', views.apply, name='apply'),
    path('faq/', views.faq, name='faq'),
    path('fees/', views.fees, name='fees'),
    path('register/', views.register, name='register'),
    path('housing/', views.housing, name='housing'),
]
