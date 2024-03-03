from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from thegamer_app.models import *


### Games
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # fields = '__all__'
        fields = ['id', 'name', 'summary', 'release_date']


class DetailedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'summary', 'release_date']
        extra_kwargs = {
            'id': {"read_only": True}
        }


### Developers
class DetailedDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
        depth = 1


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        exclude = ['games']


class CreateDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'name', "games"]
        extra_kwargs = {
            'id': {"read_only": True}
        }


### Genres

class DetailedGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['games']


class CreateGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'games']
        extra_kwargs = {
            'id': {"read_only": True}
        }


### Publishers
class DetailedPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        exclude = ['games']


class CreatePublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {"read_only": True}
        }


### Posts

class DetailedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'release_date']


class GamePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePost
        fields = ['game']


class CreatePostSerializer(serializers.ModelSerializer):
    game = GamePostSerializer(required=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'writer', 'release_date', 'game']
        extra_kwargs = {
            'id': {"read_only": True}
        }
        validators = [
            UniqueTogetherValidator(
                queryset=Post.objects.all(),
                fields=['title']
            )
        ]

    def create(self, validated_data):
        with transaction.atomic():
            game_data = validated_data['game']
            post = Post.objects.create(**validated_data)
            GamePost.objects.create(**game_data, post_id=post.id)
            return post


class GameDevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDeveloper
        # fields = '__all__'
        exclude = ['id', 'game']


class CreateGameDevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDeveloper
        fields = '__all__'