from django.conf.urls import url

from . import views

app_name = 'goal'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^today/$', views.index, name="index"),
    url(r'^(?P<goal_id>[0-9]+)/log/$', views.log, name="log"),
    url(r'^new/$', views.new_goal, name="new_goal"),
]
