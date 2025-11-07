from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Favorite
from .serializers import FavoriteSerializer
from django.contrib.auth.models import User

# Create your views here.

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = []  # Temporarily disable auth for demo

    def get_queryset(self):
        # Use first user for demo (or create one if none exists)
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demouser', password='demo123')
        return Favorite.objects.filter(user=user)

    def perform_create(self, serializer):
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demouser', password='demo123')
        serializer.save(user=user)
        
