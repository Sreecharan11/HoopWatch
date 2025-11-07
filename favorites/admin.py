from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'favorite_type', 'get_favorite_item', 'created_at']
    list_filter = ['favorite_type']
    
    def get_favorite_item(self, obj):
        if obj.player:
            return obj.player.full_name
        elif obj.team:
            return obj.team.full_name
        return "None"
    get_favorite_item.short_description = 'Item'