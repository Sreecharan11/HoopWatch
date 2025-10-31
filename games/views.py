from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Team, Game
from .serializers import TeamSerializer, GameSerializer

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'abbreviation', 'city']
    ordering_fields = ['full_name']
    ordering = ['full_name']


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['home_team__full_name', 'visitor_team__full_name']
    ordering_fields = ['date']
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset