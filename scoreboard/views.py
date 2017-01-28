from django.views.generic import DetailView

from scoreboard.models import *


class ManagementView(DetailView):
    template_name_suffix = '_manage'


class GameManagementView(ManagementView):
    model = Game


class TeamManagementView(ManagementView):
    model = Team
