from django.conf.urls import patterns, url
from rpg import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^game/$', views.game, name='game'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^battle/$', views.battle, name='battle'),
    url(r'^create_monster/$', views.create_monster, name='create_monster'),
    url(r'^create_area/$', views.create_area, name='create_area'),
    )
