from django.db import models

# Create your models here.
class Team(models.Model):
    """NBA team model which stores team information from the BallDontLie API"""

    api_id = models.IntegerField(unique=True)

    abbreviation = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    conference = models.CharField(max_length=10)
    division = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.full_name


class Game(models.Model):
    """NBA game model which stores game information from ESPN/BallDontLie API"""

    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('final', 'Final')
    ]

    api_id = models.CharField(max_length=50, unique=True)

    date = models.DateTimeField()
    season = models.IntegerField()
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='scheduled')

    home_team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='home_games',       
    )
    visitor_team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='visitor_games',
    )

    home_team_score = models.IntegerField(blank=True, null=True)
    visitor_team_score = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        indexes = [
            models.Index(fields=['-date']),
            models.Index(fields=['status']),

        ]

    def __str__(self):
        return f"{self.visitor_team.abbreviation} @ {self.home_team.abbreviation} - {self.date.strftime('%Y-%m-%d %H:%M')}"

    @property
    def is_finished(self):
        """Check if game has been played"""
        return self.status == 'final'

    @property
    def winner(self):
        """Return the winner of the game or None if the game is not finished"""
        if not self.is_finished or self.home_team_score is None:
            return None
        elif self.home_team_score > self.visitor_team_score:
            return self.home_team
        elif self.home_team_score < self.visitor_team_score:
            return self.visitor_team
        else:
            return None
