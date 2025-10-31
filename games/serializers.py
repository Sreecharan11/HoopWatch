from rest_framework import serializers
from .models import Team, Game

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    home_team_name = serializers.CharField(source='home_team.full_name', read_only=True)
    visitor_team_name = serializers.CharField(source='visitor_team.full_name', read_only=True)
    is_finished = serializers.BooleanField(read_only=True)
    winner = serializers.CharField()

    class Meta:
        model = Game
        fields = '__all__'

    def get_winner_name(self, obj):
        winner = obj.winner
        return winner.full_name if winner else None


