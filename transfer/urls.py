from django.conf.urls import patterns, url
from transfer import views


urlpatterns = [
    url(r'^$', views.transferView),
    url(r'^(\d+)/$', views.transferView),
]
