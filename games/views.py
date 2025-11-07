from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Team, Game
from .serializers import TeamSerializer, GameSerializer
from favorites.models import Favorite

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

    @action(detail=False, methods=['get'])
    def my_events(self, request):
        """Get upcoming games for user's favorited players and teams"""
        # Get user (demo user for now)
        user = User.objects.first()
        if not user:
            return Response([])
        
        # Get all user's favorites
        favorites = Favorite.objects.filter(user=user).select_related('player__team', 'team')
        
        # Collect team IDs from favorites
        team_ids = set()
        favorite_details = {}  # Map team_id to why it's favorited
        
        for fav in favorites:
            if fav.team:
                team_ids.add(fav.team.id)
                if fav.team.id not in favorite_details:
                    favorite_details[fav.team.id] = []
                favorite_details[fav.team.id].append({
                    'type': 'team',
                    'name': fav.team.full_name
                })
            
            if fav.player and fav.player.team:
                team_ids.add(fav.player.team.id)
                if fav.player.team.id not in favorite_details:
                    favorite_details[fav.player.team.id] = []
                favorite_details[fav.player.team.id].append({
                    'type': 'player',
                    'name': fav.player.full_name
                })
        
        # If no favorites, return empty list
        if not team_ids:
            return Response([])
        
        # Get upcoming games involving favorited teams
        games = Game.objects.filter(
            Q(home_team__id__in=team_ids) | Q(visitor_team__id__in=team_ids),
            status='upcoming'
        ).select_related('home_team', 'visitor_team').order_by('date')
        
        # Serialize games and add favorite info
        serializer = self.get_serializer(games, many=True)
        games_data = serializer.data
        
        # Add favorite reasons to each game
        for game_data in games_data:
            game = games.get(id=game_data['id'])
            reasons = []
            
            if game.home_team.id in favorite_details:
                reasons.extend(favorite_details[game.home_team.id])
            
            if game.visitor_team.id in favorite_details:
                reasons.extend(favorite_details[game.visitor_team.id])
            
            game_data['favorite_reasons'] = reasons
        
        return Response(games_data)