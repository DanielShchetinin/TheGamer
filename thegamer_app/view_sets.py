import django_filters
from django_filters import FilterSet
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from thegamer_app.models import *
from thegamer_app.serializers import *


class GamePageClass(PageNumberPagination):
    page_size = 5


class GameFilterSet(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    release = django_filters.CharFilter(field_name='release_date', lookup_expr='exact')
    summary = django_filters.CharFilter(field_name='summary', lookup_expr='icontains')


    class Meta:
        model = Game
        fields = ['name', 'release_date', 'summary']


class GameViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    # pagination_class = GamePageClass
    filterset_class = GameFilterSet

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedGameSerializer
        else:
            return super().get_serializer_class()

    @action(methods=['GET'], detail=True, url_path='developers')
    def developers(self, request, pk=None):
        game = self.get_object()
        developers = game.developers.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def publishers(self, request, pk=None):
        game = self.get_object()
        publishers = game.publishers.all()
        serializer = PublisherSerializer(instance=publishers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def genres(self, request, pk=None):
        game = self.get_object()
        genres = game.genres.all()
        serializer = GenreSerializer(instance=genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def posts(self, request, pk=None):
        game = self.get_object()
        posts = game.posts.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeveloperViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()
    pagination_class = GamePageClass

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedDeveloperSerializer
        else:
            return super().get_serializer_class()


class PublisherViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    pagination_class = GamePageClass

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedPublisherSerializer
        else:
            return super().get_serializer_class()


class PostViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = GamePageClass

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return DetailedPostSerializer
        elif self.action == 'create':
            return CreatePostSerializer
        else:
            return super().get_serializer_class()


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    pagination_class = GamePageClass

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedGenreSerializer
        else:
            return super().get_serializer_class()
