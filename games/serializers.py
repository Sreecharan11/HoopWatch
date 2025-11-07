from rest_framework import serializers
from .models import Team, Game

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    home_team_name = serializers.CharField(source='home_team.full_name', read_only=True)
    visitor_team_name = serializers.CharField(source='visitor_team.full_name', read_only=True)

    class Meta:
        model = Game
        fields = '__all__'