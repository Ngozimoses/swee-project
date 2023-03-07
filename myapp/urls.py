from django.urls import path
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('room', views.room, name='room'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
