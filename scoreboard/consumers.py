import json

from channels import Group

from scoreboard.models import Game, Goal


def ws_game_event(message):
    event = json.loads(message['text'])
    game = Game.objects.get(pk=event['game_id'])
    if event['event_type'] == 'g':
        Goal.objects.create(game=game,
                            team_id=event['team_id'],
                            game_time_minutes=12,
                            game_time_seconds=12,
                            player_number=12)

    Group("game").send({
        "text": message.content['text']
    })


def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("game").add(message.reply_channel)


def ws_disconnect(message):
    Group("game").discard(message.reply_channel)