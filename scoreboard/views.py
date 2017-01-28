from django.views.generic import DetailView

from scoreboard.models import *


class GameView(DetailView):
    model = Game


class GameManagementView(GameView):
    model = Game
    template_name = 'scoreboard/game_manage.html'
