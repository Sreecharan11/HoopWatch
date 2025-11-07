from django.contrib import admin
from .models import Team, Game

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'abbreviation', 'conference', 'division']
    search_fields = ['full_name', 'abbreviation']
    list_filter = ['conference', 'division']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date', 'status']
    list_filter = ['status', 'date']
    search_fields = ['home_team__full_name', 'visitor_team__full_name']