from django.conf.urls import url
from . import views

app_name = 'loginsys'
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout),

]
