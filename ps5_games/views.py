
from django.shortcuts import render
from rest_framework import generics
from .serializers import Ps5_gamesSerialzer
from .models import Ps5_games
from .permissions import IsAuthenticatedOrReadOnly

# CR views
class Ps5_gamesList(generics.ListCreateAPIView):
    queryset = Ps5_games.objects.all()
    serializer_class = Ps5_gamesSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)

# RUD view
class Ps5_gamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ps5_games.objects.all()
    serializer_class = Ps5_gamesSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)

