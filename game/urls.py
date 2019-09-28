from rest_framework import generics
from django.urls import path
from . import views

urlpatterns = [
	path('user/', views.UserList.as_view(), name=views.UserList.name),
	path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('player/', views.PlayerList.as_view(), name=views.PlayerList.name),
	path('player/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
	path('score/', views.ScoreList.as_view(), name=views.ScoreList.name),
	path('score/<int:pk>/', views.ScoreDetail.as_view(), name=views.ScoreDetail.name),
]