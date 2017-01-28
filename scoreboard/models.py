from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='+')
    visiting_team = models.ForeignKey(Team, related_name='+')
    time = models.DateTimeField()

    def home_score(self):
        return self.goal_set.filter(team=self.home_team).count()

    def __str__(self):
        return "{} - {}".format(self.home_team, self.visiting_team)


class Event(models.Model):
    game_time_minutes = models.PositiveIntegerField()
    game_time_seconds = models.PositiveIntegerField()
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    player_number = models.PositiveIntegerField()

    EVENT_TYPE_GOAL = 'G'
    EVENT_TYPE_PENALTY = 'P'
    EVENT_TYPE_TIMEOUT = 'T'

    class Meta:
        abstract = True
        ordering = ['game_time_minutes', 'game_time_seconds', ]


class Goal(Event):
    assist = models.PositiveIntegerField(null=True, blank=True)


class Penalty(Event):
    PENALTY_TYPE_T30 = 'T30'
    PENALTY_TYPE_P1 = 'P1'
    PENALTY_TYPE_P2 = 'P2'
    PENALTY_TYPE_P3 = 'P3'
    PENALTY_TYPE_EXP = 'EXP'

    PENALTY_CHOICES = [
        (PENALTY_TYPE_T30, 'Technical'),
        (PENALTY_TYPE_P1, 'Personal 1M'),
        (PENALTY_TYPE_P2, 'Personal 2M'),
        (PENALTY_TYPE_P3, 'Personal 3M'),
        (PENALTY_TYPE_EXP, 'Expulsion'),
    ]

    penalty_type = models.CharField(choices=PENALTY_CHOICES, max_length=3)
