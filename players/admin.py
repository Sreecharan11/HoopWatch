from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'team_name', 'jersey_number']
    search_fields = ['first_name', 'last_name']
    list_filter = ['position', 'team']