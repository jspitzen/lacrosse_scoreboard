from django.test import TestCase
from django.utils import timezone as tz

from scoreboard.models import *


class GameUnitTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(GameUnitTests, cls).setUpClass()
        cls.home_team = Team.objects.create(name='Home')
        cls.visiting_team = Team.objects.create(name='Away')
        cls.game = Game.objects.create(home_team=cls.home_team, visiting_team=cls.visiting_team, time=tz.now())

    def test_home_score_zero(self):
        self.assertEqual(0, self.game.home_score())

    def test_away_score_zero(self):
        self.assertEqual(1, self.game.visiting_score())
