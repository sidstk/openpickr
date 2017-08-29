from django.conf.urls import url
from . import views

#app_name = 'openpickr'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addimage/$', views.addimage, name='addimage'),
    url(r'^login/$', views.logmein, name='logmein'),
    url(r'^logout/$', views.logmeout, name='logmeout'),
    url(r'^(?P<image_id>[0-9]+)/delete/$', views.deleteimg, name='delete'),
    url(r'^signup/$', views.signup, name='signup'),

]