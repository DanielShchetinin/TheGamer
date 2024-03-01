from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from thegamer_app.serializers import *


### Games
@api_view(['GET', 'POST'])
def get_games(request: Request):
    if request.method == 'GET':
        all_games = Game.objects.all()
        if 'name' in request.query_params:
            all_games = all_games.filter(name__iexact=request.query_params['name'])
        serializer = GameSerializer(instance=all_games, many=True)
        return Response(data=serializer.data, status=200)
    if request.method == 'POST':
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_game(request: Request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'GET':
        serializer = DetailedGameSerializer(instance=game)
        return Response(data=serializer.data, status=200)
    elif request.method in ('PUT', 'PATCH'):
        serializer = DetailedGameSerializer(instance=game, data=request.data, partial=request.method == 'PATCH')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        game.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def game_developers(request: Request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'GET':
        all_developers = game.gamedeveloper_set.all()
        serializer = GameDevelopersSerializer(instance=all_developers, many=True)
        return Response(data=serializer.data, status=200)
    if request.method == 'POST':
        full_data = request.data.copy()
        full_data['game'] = game_id
        serializer = CreateGameDevelopersSerializer(data=full_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


### Developers
@api_view(['GET', 'POST'])
def get_developers(request):
    if request.method == 'GET':
        all_developers = Developer.objects.all()
        serializer = DeveloperSerializer(instance=all_developers, many=True)
        return Response(data=serializer.data, status=200)
    if request.method == 'POST':
        serializer = CreateDeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_developer(request: Request, developer_id):
    developer = get_object_or_404(Developer, id=developer_id)
    if request.method == 'GET':
        serializer = DetailedDeveloperSerializer(instance=developer)
        return Response(data=serializer.data, status=200)
    elif request.method in ('PUT', 'PATCH'):
        serializer = DetailedDeveloperSerializer(instance=developer, data=request.data,
                                                 partial=request.method == 'PATCH')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        developer.delete()
        return Response(status=204)


### Genres

@api_view(['GET', 'POST'])
def get_genres(request):
    if request.method == 'GET':
        all_genres = Genre.objects.all()
        serializer = GenreSerializer(instance=all_genres, many=True)
        return Response(data=serializer.data, status=200)
    if request.method == 'POST':
        serializer = CreateGenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_genre(request: Request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    if request.method == 'GET':
        serializer = DetailedGenreSerializer(instance=genre)
        return Response(data=serializer.data, status=200)
    elif request.method in ('PUT', 'PATCH'):
        serializer = DetailedGenreSerializer(instance=genre, data=request.data, partial=request.method == 'PATCH')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        genre.delete()
        return Response(status=204)


### Publishers
@api_view(['GET', 'POST'])
def get_publishers(request):
    if request.method == 'GET':
        all_publishers = Publisher.objects.all()
        serializer = PublisherSerializer(instance=all_publishers, many=True)
        return Response(data=serializer.data, status=200)
    if request.method == 'POST':
        serializer = CreatePublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_publisher(request: Request, publisher_id):
    publisher = get_object_or_404(Publisher, id=publisher_id)
    if request.method == 'GET':
        serializer = DetailedPublisherSerializer(instance=publisher)
        return Response(data=serializer.data, status=200)
    elif request.method in ('PUT', 'PATCH'):
        serializer = DetailedPublisherSerializer(instance=publisher, data=request.data,
                                                 partial=request.method == 'PATCH')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        publisher.delete()
        return Response(status=204)


## Posts
@api_view(['GET', 'POST'])
def get_posts(request):
    if request.method == 'GET':
        all_posts = Post.objects.all()
        serializer = PostSerializer(instance=all_posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_post(request: Request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        serializer = DetailedPostSerializer(instance=Post)
        return Response(data=serializer.data, status=200)
    elif request.method in ('PUT', 'PATCH'):
        serializer = DetailedPostSerializer(instance=Post, data=request.data, partial=request.method == 'PATCH')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        post.delete()
        return Response(status=204)
