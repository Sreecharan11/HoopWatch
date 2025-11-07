from rest_framework import viewsets
from .models import Favorite
from .serializers import FavoriteSerializer
from django.contrib.auth.models import User

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = []

    def get_queryset(self):
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demouser', password='demo123')
        return Favorite.objects.filter(user=user)

    def perform_create(self, serializer):
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demouser', password='demo123')
        serializer.save(user=user)
