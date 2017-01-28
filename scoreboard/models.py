from django.db import models

from colorful.fields import RGBColorField


class Team(models.Model):
    name = models.CharField(max_length=128)
    color = RGBColorField(null=True, blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='+')
    visiting_team = models.ForeignKey(Team, related_name='+')
    time = models.DateTimeField()

    def home_score(self):
        return self.goal_set.filter(team=self.home_team).count()

    def visiting_score(self):
        return self.goal_set.filter(team=self.visiting_team).count()

    def __str__(self):
        return "{} - {}".format(self.home_team, self.visiting_team)


class Event(models.Model):
    EVENT_TYPE_GOAL = 'G'
    EVENT_TYPE_PENALTY = 'P'
    EVENT_TYPE_TIMEOUT = 'T'

    EVENT_TYPE_CHOICES = [
        (EVENT_TYPE_GOAL, 'Goal'),
        (EVENT_TYPE_PENALTY, 'Penalty'),
        (EVENT_TYPE_TIMEOUT, 'Timeout'),
    ]

    game_time_minutes = models.PositiveIntegerField()
    game_time_seconds = models.PositiveIntegerField()
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    player_number = models.PositiveIntegerField()
    type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=1)

    class Meta:
        abstract = True
        ordering = ['game_time_minutes', 'game_time_seconds', ]

    def save(self, *args, **kwargs):
        self.type = self._event_type
        return super(Event, self).save(*args, **kwargs)


class Goal(Event):
    _event_type = 'G'
    assist = models.PositiveIntegerField(null=True, blank=True)


class Penalty(Event):
    _event_type = 'P'
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
