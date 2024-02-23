import os
import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'thegamer.settings'

import django

django.setup()

from thegamer_app.models import *

if __name__ == '__main__':
    developers = Developer.objects.all()
    for developer in developers:
        print(f"{developer}")

    # developer = Developer.objects.filter(id=2)[0]
    # game = Game.objects.filter(id=3)[0]
    # game.developers.set([developer])
    # game.save()