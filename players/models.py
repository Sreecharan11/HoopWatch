from django.db import models

class Player(models.Model):
    """NBA player model"""

    api_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    weight_pounds = models.CharField(max_length=10, blank=True)
    jersey_number = models.CharField(max_length=10, blank=True)

    team = models.ForeignKey(
        'games.Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='players'
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def team_name(self):
        return self.team.full_name if self.team else "Free Agent"