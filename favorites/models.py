from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    """NBA favorite model which stores favorite information for a user"""

    FAVORITE_CHOICES = [
        ('player', 'Player'),
        ('team', 'Team'),
        ('game', 'Game'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    favorite_type = models.CharField(max_length=10, choices=FAVORITE_CHOICES)

    player = models.ForeignKey(
        'players.Player',
        on_delete=models.CASCADE,
        related_name='favorited_by',
        null=True,
        blank=True,
    )

    team = models.ForeignKey(
        'games.Team',
        on_delete=models.CASCADE,
        related_name='favorited_by',
        null=True,
        blank=True,
    )

    game = models.ForeignKey(
        'games.Game',
        on_delete=models.CASCADE,
        related_name='favorited_by',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = [ 
            ['user', 'player'],
            ['user', 'team'],
            ['user', 'game'],
        ]
        indexes = [
            models.Index(fields=['user', 'favorite_type']),
        ]

    def __str__(self):
        if self.player:
            return f"{self.user.username} → {self.player.full_name}"
        elif self.team:
            return f"{self.user.username} → {self.team.full_name}"
        elif self.game:
            return f"{self.user.username} → {self.game}"
        return f"{self.user.username}'s favorite"
