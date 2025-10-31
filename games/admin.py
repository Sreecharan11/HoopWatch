from django.contrib import admin
from .models import Team, Game

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'abbreviation', 'conference', 'division', 'created_at']
    search_fields = ['full_name', 'abbreviation', 'city']
    list_filter = ['conference', 'division']
    ordering = ['full_name']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['get_game_display', 'date', 'status', 'home_team_score', 'visitor_team_score', 'season']
    list_filter = ['status', 'season', 'date']
    search_fields = ['home_team__full_name', 'visitor_team__full_name']
    date_hierarchy = 'date'
    ordering = ['-date']
    
    def get_game_display(self, obj):
        return str(obj)
    get_game_display.short_description = 'Game'
