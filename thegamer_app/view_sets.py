from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from thegamer_app.models import Game
from thegamer_app.serializers import GameSerializer, DetailedGameSerializer, PostSerializer, DetailedPostSerializer, \
    CreatePostSerializer, DeveloperSerializer, PublisherSerializer

class GamePageClass(PageNumberPagination):
    page_size = 5

class GameViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    pagination_class = GamePageClass

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedGameSerializer
        else:
            return super().get_serializer_class()

    @action(methods=['GET'], detail=True)
    def developers(self):
        game = self.get_object()
        developers = game.gamedeveloper_set.all()
        serializer = DeveloperSerializer(instance=developers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def publishers(self):
        game = self.get_object()
        publishers = game.gamepublisher_set.all()
        serializer = PublisherSerializer(instance=publishers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class PostViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = PostSerializer
    queryset = Game.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedPostSerializer
        if self.action == 'create':
            return CreatePostSerializer
        else:
            return super().get_serializer_class()
