from django.conf.urls import url
from income import views


urlpatterns = [
    url(r'^$', views.incomeView),
    url(r'^(\d+)/$', views.incomeView),
]
