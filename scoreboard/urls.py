from django.conf.urls import url

from scoreboard.views import GameManagementView

urlpatterns = [
    url(r'(?P<pk>\d+)/manage/', GameManagementView.as_view(), name='manage_game'),
    url(r'(?P<pk>\d+)/', GameManagementView.as_view(), name='manage_game'),
]
