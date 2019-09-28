from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    name = 'player-list'

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'

class ScoreList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = ScoreSeiralizer
    filter_fields = '__all__'
    filter_backends = (filters.DjangoFilterBackend,)
    name = 'score-list'
class ScoreDetail(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = ScoreSeiralizer
    name = 'score-detail'