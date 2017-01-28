import json

from channels import Group


def ws_game_event(message):
    event = json.loads(message['text'])
    Group("game").send({
        "text": message.content['text']
    })


def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("game").add(message.reply_channel)


def ws_disconnect(message):
    Group("game").discard(message.reply_channel)