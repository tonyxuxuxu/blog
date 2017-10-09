from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'blog'
urlpatterns = [
               url(r'^admin/', admin.site.urls),
               url(r'^$', views.index, name='index'),
               url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
               ]
