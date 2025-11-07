from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Team, Game
from .serializers import TeamSerializer, GameSerializer
from favorites.models import Favorite

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'abbreviation', 'city']


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=False, methods=['get'])
    def my_events(self, request):
        """Get upcoming games for user's favorited players and teams"""
        user = User.objects.first()
        if not user:
            return Response([])
        
        favorites = Favorite.objects.filter(user=user).select_related('player__team', 'team')
        
        team_ids = set()
        favorite_details = {}
        
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
        
        if not team_ids:
            return Response([])
        
        games = Game.objects.filter(
            Q(home_team__id__in=team_ids) | Q(visitor_team__id__in=team_ids),
            status='upcoming'
        ).select_related('home_team', 'visitor_team').order_by('date')
        
        serializer = self.get_serializer(games, many=True)
        games_data = serializer.data
        
        for game_data in games_data:
            game = games.get(id=game_data['id'])
            reasons = []
            
            if game.home_team.id in favorite_details:
                reasons.extend(favorite_details[game.home_team.id])
            
            if game.visitor_team.id in favorite_details:
                reasons.extend(favorite_details[game.visitor_team.id])
            
            game_data['favorite_reasons'] = reasons
        
        return Response(games_data)