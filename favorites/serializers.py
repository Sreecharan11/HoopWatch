from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='player.full_name', read_only=True)
    team_name = serializers.CharField(source='team.full_name', read_only=True)

    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['user']