from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'favorite_type', 'get_favorite_item', 'created_at']
    list_filter = ['favorite_type', 'created_at']
    search_fields = ['user__username', 'player__first_name', 'player__last_name', 'team__full_name']
    ordering = ['-created_at']
    
    def get_favorite_item(self, obj):
        if obj.player:
            return obj.player.full_name
        elif obj.team:
            return obj.team.full_name
        elif obj.game:
            return str(obj.game)
        return "None"
    get_favorite_item.short_description = 'Favorited Item'
