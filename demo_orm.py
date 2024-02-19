import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'thegamer.settings'

import django

django.setup()

from thegamer_app.models import *

if __name__ == '__main__':
    games = Game.objects.all()
    for game in games:
        print(game.name, game.summary)
