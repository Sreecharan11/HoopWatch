from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'position', 'team__full_name']
    ordering_fields = ['last_name', 'first_name', 'position', 'team__full_name']
    ordering = ['last_name', 'first_name']

