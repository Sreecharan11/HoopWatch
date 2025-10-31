from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'