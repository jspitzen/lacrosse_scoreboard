from channels.routing import route

from scoreboard.consumers import *

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_game_event),
    route("websocket.disconnect", ws_disconnect),
]
