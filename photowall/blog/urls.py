from django.urls import path, include, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]