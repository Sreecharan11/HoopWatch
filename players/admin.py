from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'team_name', 'jersey_number', 'height', 'weight_pounds']
    search_fields = ['first_name', 'last_name']
    list_filter = ['position', 'team', 'country']
    ordering = ['last_name', 'first_name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'position', 'team')
        }),
        ('Physical Stats', {
            'fields': ('height', 'weight_pounds', 'jersey_number')
        }),
        ('Background', {
            'fields': ('college', 'country', 'draft_year', 'draft_round', 'draft_number')
        }),
        ('API', {
            'fields': ('api_id',)
        }),
    )
