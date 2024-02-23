from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from thegamer_app.models import *
from thegamer_app.serializers import *


# Create your views here.
@api_view(['GET'])
def get_games(request: Request):
    all_games = Game.objects.all()
    if 'name' in request.query_params:
        all_games = all_games.filter(name__iexact=request.query_params['name'])
    serializer = GameSerializer(instance=all_games, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def get_developers(request):
    all_developers = Developer.objects.all()
    serializer = DeveloperSerializer(instance=all_developers, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def get_genres(request):
    all_genres = Genre.objects.all()
    serializer = GenreSerializer(instance=all_genres, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def get_publishers(request):
    all_publishers = Publisher.objects.all()
    serializer = PublisherSerializer(instance=all_publishers, many=True)
    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def get_posts(request):
    all_posts = Post.objects.all()
    serializer = PostSerializer(instance=all_posts, many=True)
    return Response(data=serializer.data, status=200)
