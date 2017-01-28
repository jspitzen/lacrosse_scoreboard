from django.conf.urls import url

from scoreboard.views import GameManagementView, GameView

urlpatterns = [
    url(r'(?P<pk>\d+)/manage/$', GameManagementView.as_view(), name='manage_game'),
    url(r'(?P<pk>\d+)/$', GameView.as_view(), name='game'),
]
