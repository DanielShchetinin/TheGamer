from rest_framework.viewsets import ModelViewSet

from thegamer_app.models import Game
from thegamer_app.serializers import GameSerializer

class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
