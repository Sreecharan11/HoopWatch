from django.db import models

class Team(models.Model):
    """NBA team model"""

    api_id = models.IntegerField(unique=True)
    abbreviation = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    conference = models.CharField(max_length=10)
    division = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Game(models.Model):
    """NBA game model"""

    api_id = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField()
    season = models.IntegerField()
    status = models.CharField(max_length=20, default='upcoming')

    home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='home_games')
    visitor_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='visitor_games')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.visitor_team.abbreviation} @ {self.home_team.abbreviation} - {self.date.strftime('%Y-%m-%d')}"
