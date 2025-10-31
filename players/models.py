from django.db import models

# Create your models here.

class Player(models.Model):
    """Nba player model which stores player information from the BallDontLie API"""

    api_id = models.IntegerField(unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


    college = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=10, blank=True)
    weight_pounds = models.CharField(max_length=10, blank=True)
    jersey_number = models.CharField(max_length=10, blank=True)

    draft_year = models.IntegerField(null=True, blank=True)
    draft_round = models.IntegerField(null=True, blank=True)
    draft_number = models.IntegerField(null=True, blank=True)

    team = models.ForeignKey(
        'games.Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='players'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def team_name(self):
        return self.team.full_name if self.team else "Free Agent"