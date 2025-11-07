from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    """User's favorite players and teams"""

    FAVORITE_CHOICES = [
        ('player', 'Player'),
        ('team', 'Team'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    favorite_type = models.CharField(max_length=10, choices=FAVORITE_CHOICES)
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey('games.Team', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = [['user', 'player'], ['user', 'team']]

    def __str__(self):
        if self.player:
            return f"{self.user.username} → {self.player.full_name}"
        elif self.team:
            return f"{self.user.username} → {self.team.full_name}"
        return f"{self.user.username}'s favorite"
