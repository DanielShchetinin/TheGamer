from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)
    summary = models.CharField(null=True, blank=True, max_length=1028)
    release_date = models.DateField(null=True, blank=True)

    developers = models.ManyToManyField("Developer", through="GameDeveloper")
    genres = models.ManyToManyField("Genre", through="GameGenre")
    publishers = models.ManyToManyField("Publisher", through="GamePublisher")
    posts = models.ManyToManyField("Post", through="GamePost")

    class Meta:
        db_table = 'games'

    def __str__(self):
        return f"[ID: {self.id}] - {self.name}"


class Developer(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)

    games = models.ManyToManyField("Game", through="GameDeveloper")

    class Meta:
        db_table = 'developers'

    def __str__(self):
        return f"[ID: {self.id}] - {self.name}"


class Publisher(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        db_table = 'publishers'


class Genre(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)

    class Meta:
        db_table = 'genres'


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=128)
    content = models.TextField(null=False, blank=False)
    release_date = models.DateField(null=False, blank=False)
    writer = models.CharField(null=False, blank=False, max_length=64)

    class Meta:
        db_table = 'posts'


class GameDeveloper(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    developer = models.ForeignKey("Developer", on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_developers'


class GameGenre(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_genres'


class GamePublisher(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_publishers'


class GamePost(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_posts'
